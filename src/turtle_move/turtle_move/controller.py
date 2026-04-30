import rclpy
import math
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from shape_interface.srv import DrawShape


class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.msg = Twist()

        self.srv = self.create_service( 
            DrawShape,'draw_shape', self.draw_shape_callback
            )

    def draw_shape_callback(self, request, response):
        if request.shape == "square":
            self.draw_square()
            response.success = True
            response.message = "Square drawn"
        elif request.shape == "circle":
            self.draw_circle()
            response.success = True
            response.message = "circle drawn"
        elif request.shape == "triangle":
            self.draw_triangle()
            response.success = True
            response.message = "triangle drawn"
        elif request.shape == "Rectangle":
            self.draw_rectangle()
            response.success = True
            response.message = "rectangle drawn"
        elif request.shape == "polygon":
            self.draw_polygon()
            response.success = True
            response.message = "polygon drawn"
        elif request.shape == "hexagon":
            self.draw_hexagon()
            response.success = True
            response.message = "hexagon drawn"
        else:
            response.success = False
            response.message = "Unknown shape"

        return response


    def draw_circle(self):
        self.msg.linear.x = 1.0
        self.msg.angular.z = 1.0
        start_time = time.time()

        while (time.time() - start_time) <6.28: 
            self.publisher_.publish(self.msg)


    def draw_triangle(self):
        for i in range(3):
            self.msg.linear.x = 2.0
            self.msg.angular.z = 0.0
            self.publisher_.publish(self.msg)
            time.sleep(1)

            self.msg.linear.x = 0.0
            self.msg.angular.z = 2.1
            self.publisher_.publish(self.msg)
            time.sleep(1)

    def draw_square(self):
        for _ in range(4):
            self.msg.linear.x = 2.0
            self.msg.angular.z = 0.0
            self.publisher_.publish(self.msg)
            time.sleep(1)

            self.msg.linear.x = 0.0
            self.msg.angular.z = 1.57
            self.publisher_.publish(self.msg)
            time.sleep(1)

    def draw_rectangle(self): 
        for i in range(4):

            if i == 0 or i == 2:
                y = 1.0
            else:
                y = 2.0

            self.msg.linear.x = y
            self.msg.angular.z = 0.0
            self.publisher_.publish(self.msg)
            time.sleep(1)

            self.msg.linear.x = 0.0
            self.msg.angular.z = 1.57
            self.publisher_.publish(self.msg)
            time.sleep(1)

    def draw_polygon(self):
        for i in range(5):
            self.msg.linear.x = 2.0
            self.msg.angular.z = 0.0
            self.publisher_.publish(self.msg)
            time.sleep(1)

            self.msg.linear.x = 0.0
            self.msg.angular.z = 1.258
            self.publisher_.publish(self.msg)
            time.sleep(1)

    def draw_hexagon(self):
        for i in range(6):
            self.msg.linear.x = 2.0
            self.msg.angular.z = 0.0
            self.publisher_.publish(self.msg)
            time.sleep(1)

            self.msg.linear.x = 0.0
            self.msg.angular.z = 1.04
            self.publisher_.publish(self.msg)
            time.sleep(1)

def main():
    rclpy.init()
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
