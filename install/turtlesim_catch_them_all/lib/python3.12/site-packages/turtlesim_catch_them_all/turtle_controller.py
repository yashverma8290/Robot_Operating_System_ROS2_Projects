#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from functools import partial
from geometry_msgs.msg import Twist
from my_robot_interfaces.msg import Turtle
from my_robot_interfaces.msg import TurtleArray
from my_robot_interfaces.srv import CatchTurtle

class TurtleControllerNode(Node):  
    def __init__(self):
        super().__init__("turtle_controller")
        self.declare_parameter("catch_closest_turtle_first", True)
        self.catch_closest_turtle_first_ = self.get_parameter("catch_closest_turtle_first").value

        # Stores the current target turtle to catch (updated from alive_turtles topic)
        self.turtle_to_catch_: Turtle = None

        self.catch_closest_turtle_first_ = True
        
        # Stores the current pose of turtle1 (updated from /turtle1/pose topic)
        self.pose_: Pose = None
        
        # Publisher to send velocity commands to turtle1
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        # Subscriber to get pose updates of turtle1 (Published by turtlesim_node)
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.callback_pose, 10)

        # Subscriber to get list of currently alive turtles (Published by another node)
        self.alive_turtles_subscriber_ = self.create_subscription(TurtleArray, "alive_turtles", self.callback_alive_turtles, 10)

        # Service client to call the catch_turtle service when a turtle is reached
        self.catch_turtle_client_ = self.create_client(CatchTurtle, "catch_turtle")

        # Timer to repeatedly run control logic every 0.01 seconds
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        
    # Callback to update the current pose of turtle1
    def callback_pose(self, pose: Pose):
        self.pose_ = pose

    # Callback to update the current target turtle to catch (selects the first one in the list)
    def callback_alive_turtles(self, msg: TurtleArray):
        if len(msg.turtles) > 0:
            if self.catch_closest_turtle_first_:
                closest_turtle = None
                closest_turtle_distance = None

                for turtle in msg.turtles:
                    dist_x = turtle.x -self.pose_.x
                    dist_y = turtle.y - self.pose_.y
                    distance = math.sqrt(dist_x* dist_x + dist_y*dist_y)
                    if closest_turtle == None or distance < closest_turtle_distance:
                        closest_turtle = turtle
                        closest_turtle_distance = distance
                self.turtle_to_catch_ = closest_turtle
            else:
                self.turtle_to_catch_ = msg.turtles[0]

    # Main control loop: Move toward the target turtle and catch it when close
    def control_loop(self):
        if self.pose_ is None or self.turtle_to_catch_ is None:
            return

        # Calculate distance to the target turtle
        dist_x = self.turtle_to_catch_.x - self.pose_.x
        dist_y = self.turtle_to_catch_.y - self.pose_.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)

        cmd = Twist()

        if distance > 0.5:
            # Set forward speed proportional to the distance
            cmd.linear.x = distance

            # Calculate angle to the target and adjust orientation
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta

            # Normalize the angle difference to [-π, π]
            if diff > math.pi:
                diff -= 2 * math.pi
            elif diff < -math.pi:
                diff += 2 * math.pi

            # Set angular speed proportional to angle difference
            cmd.angular.z = 6 * diff
        else:
            # Turtle is close enough — stop and catch it
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.call_catch_turtle_service(self.turtle_to_catch_.name)
            self.turtle_to_catch_ = None
         
        # Publish velocity command (turtlesim_node subscribes to this topic to move turtle)
        self.cmd_vel_publisher_.publish(cmd)

    # Call the catch_turtle service to remove the caught turtle
    def call_catch_turtle_service(self, turtle_name):
        while not self.catch_turtle_client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for catch_turtle service...")

        request = CatchTurtle.Request()
        request.name = turtle_name

        # Call the service asynchronously
        future = self.catch_turtle_client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_catch_turtle_service, turtle_name=turtle_name))

    # Callback when catch_turtle service responds
    def callback_call_catch_turtle_service(self, future, turtle_name):
        response: CatchTurtle.Response = future.result()
        if not response.success:
            self.get_logger().error("Turtle " + turtle_name + " could not be removed")

# Entry point of the program
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
