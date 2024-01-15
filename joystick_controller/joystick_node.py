#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoystickControllerNode(Node):

    def __init__(self):
        super().__init__("joystick_controller_node")
        self.get_logger().info("Joystick Controller Node Initialised")
        self.joy_subscriber = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10
        )
        self.robot_command_publisher = self.create_publisher(
            Twist,
            'vrep/twistCommand',
            10
        )

    def joy_callback(self, msg):
        linear_velocity = msg.axes[1]
        angular_velocity = msg.axes[3]

        # Log the velocity
        # self.get_logger().info(f"Linear Velocity: {linear_velocity}, Angular Velocity: {angular_velocity}")

        msg = Twist()

        msg.linear.x = linear_velocity
        msg.angular.z = angular_velocity

        self.robot_command_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = JoystickControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()