import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mrdulcich/DevProjs/RoboticsProjects/ros2_ws/src/install/turtlebot3_behavior_pkg'
