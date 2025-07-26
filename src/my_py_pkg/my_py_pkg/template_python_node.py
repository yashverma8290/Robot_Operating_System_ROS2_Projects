#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyCustomNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("node_name") # MODIFY NAME



def main(args=None):
    rclpy.init(args=args)
    node=MyCustomNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__== "__main__":
    main()


# after making new code
# 1) chmod +x code_name.py 
# 2) go to setup.py and add the the line 
  #  eg. "shortcut name = my_py_pkg.code_name:main"
# 3)colcon build --packages-select my_py_pkg --symlink-install 
#   colcon build should be done inside ros2_ws and nothing else
# 4) after that we can source it so that our terminal get to know the changes made my the workspace






# node ek variable hai jisa value node_name hai , think of it like a=4, then a is the variable and 5 is the value given to it
