from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    # Get path to the URDF file
    urdf_path = os.path.join(
        get_package_share_path('my_robot_description'),
        'urdf',
        'my_robot.urdf'
    )

    # Read the URDF file content
    with open(urdf_path, 'r') as infp:
        robot_description = infp.read()

    # Define robot_state_publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    # Define joint_state_publisher_gui node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    # Define rviz2 node
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(
            get_package_share_path('my_robot_description'),
            'rviz',
            'urdf_config.rviz'
        )],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])
