
Open Terminal and source the following files, use your own filepath if you have stored them somewhere else
If you don't have them, make sure to install them.
# Navigate to ros2_ws then perform the following commands
cd ros2_ws

# For ROS2, TurtleBot3, and PKG ros2_ws
source /opt/ros/humble/setup.bash
source ~/turtlebot3_ws/install/setup.bash
source install/setup.bash

# Change the filepaths if any of these differ 

# Run
colcon build

# Teleoperation with keyboard
# Launch the following in different terminals make sure to source humble and turtlebot3 and ros2_ws
# Launch the turtlebot gazebo
ros2 launch turtlebot3_behavior_pkg teleop_launch.py

Then

# Launch the keyboard
ros2 launch turtlebot3_behavior_pkg teleop_node.py
# OR: If the command above doesen't work open a new terminal source ROS2 and TurtleBot3 and run the command below
ros2 run turtlebot3_teleop teleop_keyboard

OR

# Movement based on programmed behavior
ros2 launch turtlebot3_behavior_pkg behavior_launch.py




# Other commands
# Launching rviz for making the config file
ros2 run rviz2 rviz2