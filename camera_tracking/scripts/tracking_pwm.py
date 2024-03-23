#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
import numpy as np

class CameraTracking(Node):
    def __init__(self):
        super().__init__('camera_tracking')
        self.shape_centroid = self.create_subscription(
            Point,
            'shape_centroid',
            self.tracking_callback,
            10)  # openCV 객체 검출정보(검출된 도형의 중심)

        self.PWM_publisher = self.create_publisher(Float32, 'motor_control', 10)  # 아두이노로 보낼 PWM DATA
        self.center_x = 320  # 카메라 화각 중심 x좌표 [pixel]
        self.pwm = 90        # pwm 초기값(서보모터 정지상태)

        ## pixel  : 640X480
        ## axis_X : 오른쪽 (+)  [0 <= axis_X <= 640]
        ## axis_Y : 아래쪽 (+)  [0 <= axis_Y <= 480]

    def tracking_callback(self, msg):

        x_value = float(msg.x)

        if self.center_x - 125 <= x_value <= self.center_x + 125:
            self.pwm = 90  # 서보모터 정지

        elif x_value < self.center_x - 100:
            self.pwm = (9/32)*(640-x_value)  # 서보모터 반시계방향 회전

        elif x_value > self.center_x + 100:
            self.pwm = (9/32)*(640-x_value)  # 서보모터 시계방향 회전

        pwm_msg = Float32()
        pwm_msg.data = float(self.pwm)
        self.PWM_publisher.publish(pwm_msg)


def main():
    rclpy.init()
    camera_tracking = CameraTracking()

    try:
        rclpy.spin(camera_tracking)
    except KeyboardInterrupt:
        pass

    camera_tracking.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

######### 정밀화 필요 #########################################

# 1. boundingbox의 중심이 이동하는 속도 계산
#    - centeroid 미분
# 2. boundingbox의 중심이 이동하는 속도에 따른 서보모터 회전속도 결정
# 3. 서보모터 PD제어

######### 2024.02.05 #######################################
# 1. ROS에서 생성한 토픽을 아두이노에서 받아오는 데 delay가 있음
#    - delay되지 않도록 조정 필요 (Hz?? -> baud rate 조정??)
# 2. Arduino-ide를 켜놓은 상태에서 micro-ROS를 실행하면 error발생하는 경우가 많음
#    -> micro-ROS를 실행한 후 Arduino-ide를 켜면(serial monitor 체크를 위해) 아무런 문제 X
#    - 이유가 뭔지 알아볼 필요 O