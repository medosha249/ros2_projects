import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class LEDController(Node):
    def __init__(self):
        super().__init__('led_controller')
        self.subscription = self.create_subscription(
            String,
            'led_command',
            self.listener_callback,
            10
        )
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600)  
        self.get_logger().info('LED controller node started.')

    def listener_callback(self, msg):
        command = msg.data.strip().upper()
        self.get_logger().info(f'Received command: {command}')
        if command in ['ON', 'OFF']:
            self.serial_port.write((command + '\n').encode())

def main(args=None):
    rclpy.init(args=args)
    node = LEDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
