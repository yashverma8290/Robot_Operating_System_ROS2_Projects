cmake_minimum_required(VERSION 3.8)
project(my_robot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
     "msg/HardwareStatus.msg"
     "msg/LedStateArray.msg"
     "msg/Turtle.msg"
     "msg/TurtleArray.msg"
     "srv/ComputeRectangleArea.srv"
     "srv/SetLed.srv"
    
 )

ament_export_dependencies(rosidl_default_runtime)

ament_package()


#Jaise kitchen me recipe batati
# hai ki kaunse ingredients use karne hain, kis order me aur kitna time, waise hi CMakeLists.txt software build karne ki recipe hai.


#Just like a recipe in the kitchen tells you which ingredients to use, in what order, and for how long — the CMakeLists.txt file is a recipe for building software.

