import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        self.subscriber = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            10
        )
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.twist = Twist()

    def lidar_callback(self, msg):
        front_distance = msg.ranges[0]  # Distance directly in front
        left_distance = msg.ranges[25]   # Distance to the left
        right_distance = msg.ranges[335]  # Distance to the right

        # Log the sensor readings to the console
        self.get_logger().info(
            f'Front Distance: {front_distance:.2f}, '
            f'Left Distance: {left_distance:.2f}, '
            f'Right Distance: {right_distance:.2f}'
        )

        if front_distance < 0.5:  # Obstacle detected in front
            if right_distance > 0.3:
                # Turn right while moving forward slightly
                self.twist.linear.x = 0.1  # Small forward movement
                self.twist.angular.z = 7.5  # Turn right - this drastic for more interesting behavior
            else:
                # If no space to turn right, back up slightly and turn left
                self.twist.linear.x = -0.1  # Small backward movement
                self.twist.angular.z = 0.5  # Turn left
        else:
            # Before moving forward, check the left and right distances
            if left_distance > 0.3 and right_distance > 0.3:
                # Clear path, move forward
                self.twist.linear.x = 0.2  # Move forward
                self.twist.angular.z = 0.0  # No turning
            else:
                # If there is no clear path, continue turning right
                self.twist.linear.x = 0.0  # Stay still
                self.twist.angular.z = 0.5  # Keep turning right

    def timer_callback(self):
        self.publisher.publish(self.twist)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
