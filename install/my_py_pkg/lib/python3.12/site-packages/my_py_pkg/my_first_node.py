import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")  # Give the robot (node) a name
        self.counter_=0
        self.get_logger().info("Hello world")  # Make it speak once
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("hello " + str(self.counter_))
        self.counter_+=1


def main(args=None):
    rclpy.init(args=args)           # Start ROS 2 engine
    node = MyNode()                 # Build your robot
    rclpy.spin(node)                # Keep the robot running
    rclpy.shutdown()                # Clean shutdown when stopped

if __name__ == "__main__":
    main()
