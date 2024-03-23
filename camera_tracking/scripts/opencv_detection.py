#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point 
from cv_bridge import CvBridge
import cv2
import numpy as np

class ShapeColorDetector(Node):
    def __init__(self):
        super().__init__('shape_color_detector')
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.image_callback,
            10)
        self.publisher = self.create_publisher(Point, 'shape_centroid', 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except CvBridgeError as e:
            self.get_logger().error(f"Error converting ROS2 image: {e}")
            return

        processed_image = self.detect_shapes_and_colors(cv_image)

        cv2.imshow('Processed Image', processed_image)
        cv2.waitKey(1)

    def detect_shapes_and_colors(self, image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_color = np.array([0, 100, 100])  # HSV 최저
        upper_color = np.array([5, 255, 255])  # HSV 최고

        color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            num_vertices = len(approx)

            if num_vertices == 3: # 절점 개수
                shape = "Triangle"
            else:
                continue

            M = cv2.moments(approx)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                centroid_msg = Point()
                centroid_msg.x = float(cx)
                centroid_msg.y = float(cy)
                centroid_msg.z = 0.0  
                self.publisher.publish(centroid_msg)

            cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

            cv2.putText(image, shape, tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        return image

def main(args=None):
    rclpy.init(args=args)
    shape_color_detector = ShapeColorDetector()
    rclpy.spin(shape_color_detector)
    shape_color_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()