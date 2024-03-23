#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=["ros2", "run", "usb_cam", "usb_cam_node_exe", "--ros-args", "--params-file", "/home/sun/ros2_ws/src/usb_cam-ros2/config/params_1.yaml"],
            output="screen"
        ),
        Node(
            package='camera_tracking',
            executable='opencv_detection.py',
            name='opencv_detection',
            output='screen',
            emulate_tty=True,
        ),
        Node(
            package='camera_tracking',
            executable='tracking_pwm.py',
            name='tracking_pwm',
            output='screen',
            emulate_tty=True,
        ),
    ])
