# ~/turtlebot3_behavior_pkg/launch/teleop_launch.py

import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot3_teleop',
            executable='teleop_keyboard',
            name='teleop_node',
            output='screen',
            prefix='gnome-terminal -- bash -c "source /opt/ros/humble/setup.bash; source ~/turtlebot3_ws/install/setup.bash; ros2 run teleop_twist_keyboard teleop_twist_keyboard; exec bash"',  # Full command
        ),
    ])