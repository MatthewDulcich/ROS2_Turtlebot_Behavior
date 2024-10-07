# TurtleBot3 Behavior Package

This README provides instructions for setting up and running the TurtleBot3 behavior package using ROS2.

## Prerequisites

Make sure you have installed ROS2 and the TurtleBot3 packages. If you haven't, please install them before proceeding.

## Setup Instructions

1. **Open terminal** and install this package into ros2_ws/src, or if you clone this repo clone it into a folder named ros2_ws
    ```bash
    git clone https://github.com/MatthewDulcich/ROS2_Turtlebot_Behavior.git
    ```

2. **Run commands** and source the following files. Adjust the file paths if you've stored them elsewhere:

    ```bash
    source /opt/ros/humble/setup.bash
    source ~/turtlebot3_ws/install/setup.bash
    source ~/ros2_ws/install/setup.bash
    ```

3. **Navigate to your workspace**:

    ```bash
    cd ros2_ws
    ```

4. Ensure the package is located in the `ros2_ws/src` directory. If you cloned the repository, the main folder should be `ros2_ws`.

## Building the Package

Build the package using:

```bash
colcon build
```

# Teleoperation with Keyboard

To control the TurtleBot using the keyboard, follow these steps. Make sure to launch the commands in different terminals and source the necessary setups for ROS2, TurtleBot3, and your workspace.

```bash
# Step 1: Launch the TurtleBot in Gazebo
ros2 launch turtlebot3_behavior_pkg teleop_launch.py

# Step 2: Launch the Keyboard Teleoperation
ros2 launch turtlebot3_behavior_pkg teleop_node.py

# Alternative Method: If the command above doesn't work, open a new terminal, 
# source ROS2 and TurtleBot3 again, and run:
ros2 run turtlebot3_teleop teleop_keyboard
```

# Movement Based on Programmed Behavior

To launch the turtlebot with autonomous behavior, follow these steps. Make sure to launch the commands in terminals properly sourced with the commands for ROS2, TurtleBot3, and your workspace.

```bash
ros2 launch turtlebot3_behavior_pkg behavior_launch.py
```