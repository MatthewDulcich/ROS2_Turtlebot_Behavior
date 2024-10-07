from setuptools import find_packages, setup
from glob import glob

package_name = 'turtlebot3_behavior_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/behavior_launch.py', 'launch/teleop_launch.py']),
        ('share/' + package_name + '/turtlebot3_behavior_pkg', ['turtlebot3_behavior_pkg/teleop_node.py','turtlebot3_behavior_pkg/behavior_node.py' ]),
        ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),  

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mrdulcich',
    maintainer_email='emailhiddenforgithubpush',
    description='simple braitenberg vehicle behavior for turtlebot3',
    license='UNLICENSE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'behavior_node = turtlebot3_behavior_pkg.behavior_node:main',
        ],
    },
)
