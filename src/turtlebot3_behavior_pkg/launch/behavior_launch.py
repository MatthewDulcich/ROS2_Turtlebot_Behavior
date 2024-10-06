# ~/turtlebot3_behavior_pkg/launch/behavior_launch.py

import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    return LaunchDescription([
        # Include the Gazebo launch file
        IncludeLaunchDescription(
            launch_description_source=PathJoinSubstitution([
                FindPackageShare('turtlebot3_gazebo'),
                'launch',
                'turtlebot3_world.launch.py',  # Can also be turtlebot3_house.launch.py and empty_world.launch.py
            ]),
        ),

        # Launch the autonomous behavior node
        Node(
            package='turtlebot3_behavior_pkg',
            executable='behavior_node',
            name='behavior_node',
            output='screen',
        ),

        # Launch RViz
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=['-d', PathJoinSubstitution([
                FindPackageShare('turtlebot3_behavior_pkg'),
                'rviz',
                'turtlebot3_behavior.rviz'
            ])],
            parameters=[{'use_sim_time': True}]  # Use simulation time
        ),

    ])


