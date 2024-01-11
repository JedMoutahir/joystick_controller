#!/usr/bin/env python3

import rclpy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoystickControllerNode:

    def __init__(self):
        self.node = rclpy.create_node('joystick_controller_node')
        self.joy_subscriber = self.node.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10
        )
        self.cmd_publisher = self.node.create_publisher(Twist, 'cmd_vel', 10)
        self.twist_msg = Twist()

    def joy_callback(self, msg):
        # Adjust the indices based on your joystick configuration
        linear_velocity = msg.axes[1]  # Change if needed
        angular_velocity = msg.axes[3]  # Change if needed

        self.twist_msg.linear.x = linear_velocity
        self.twist_msg.angular.z = angular_velocity

        self.cmd_publisher.publish(self.twist_msg)

def main(args=None):
    rclpy.init(args=args)
    joystick_controller = JoystickControllerNode()
    rclpy.spin(joystick_controller.node)
    joystick_controller.node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
