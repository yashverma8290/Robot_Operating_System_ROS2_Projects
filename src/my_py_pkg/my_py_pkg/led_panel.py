#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node  
from my_robot_interfaces.msg import LedStateArray  
from my_robot_interfaces.srv import SetLed  


class LEDPanelNode(Node):  
    def __init__(self):
        super().__init__("led_panel")  
        
      
        self.led_states_ = [0, 0, 0]

        self.led_states_pub_ = self.create_publisher(LedStateArray, "led_panel_state", 10)
        self.led_states_timer_ = self.create_timer(5.0, self.publish_led_states)
        self.set_led_service_ = self.create_service(SetLed, "set_led", self.callback_set_led_service)
        self.get_logger().info("LED panel node has been started") 

    # Function to publish current LED states to the topic
    def publish_led_states(self):
        msg = LedStateArray()  # Create an instance of custom message
        msg.led_states = self.led_states_  
        self.led_states_pub_.publish(msg)  

    # Callback function for the "set_led" service
    def callback_set_led_service(self, request: SetLed.Request, response: SetLed.Response):
        led_number_to_update = request.led_number  # Get which LED client wants to update
        new_led_state = request.led_states   # Get the desired state: 0 = OFF, 1 = ON

        
        if led_number_to_update >= len(self.led_states_) or led_number_to_update < 0:
            response.success = False
            return response
        
        
        if new_led_state not in [0, 1]:
            response.success = False
            return response  

        
        self.led_states_[led_number_to_update] = new_led_state
        
        # Optionally publish updated state immediately after change
        self.publish_led_states()
        
        # Mark the response as success = True
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args) 
    node = LEDPanelNode()  
    rclpy.spin(node)  
    rclpy.shutdown() 


if __name__ == "__main__":
    main()






'''
                                              CODE SUMMARY IN HINGLISH
Ek baar ek robot tha jiska naam tha LEDPanelNode. Ye robot ka kaam tha apne LED panel ki states ko monitor karna aur
update karna. Robot ka internal system 3 LEDs ko track karta tha, jinmein sabhi initially OFF the, matlab [0, 0, 0].
Har 5 second baad, robot apne internal LED states ko ek ROS topic ke through duniya ko batata tha, iske liye usne ek
publisher create kiya tha jo LedStateArray naam ke custom message ko publish karta tha. Is message mein LED states ki
array hoti thi, jaise ki [0, 1, 0] agar kuch LEDs on ho.

Par robot ke paas ek aur khaas feature tha – ek service jo kisi bhi client ko allow karti thi ki wo specific LED ko on
ya off kar sake. Is service ko set_led kaha jata tha. Jab client is service ko call karta tha, robot uss LED ki state
ko update karta tha aur phir se updated LED states ko publish karta tha.

Agar koi client galat LED number ya invalid state (jaise 2 ya 3 LED number, ya -1 state) bhejta, toh robot apne response
mein false bhej deta, aur agar sab kuch sahi hota, toh true bhej kar batata tha ki LED successfully update ho gayi.

Aise, ye robot har 5 second mein apne LED panel ki state ko monitor karta, publish karta, aur clients ko apne LED panel
ko remotely control karne ka ek tarika deta. Aur is tarah se, LEDPanelNode robot apne ROS-based communication mein kaafi
smart aur responsive tha!  

'''