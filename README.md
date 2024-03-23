# ![image](https://github.com/gabrielsunhyuck/object-tracking-usbcam/assets/163500499/2d905299-a556-482f-b833-5aa2f788e0c9) object-tracking-usbcam

### **You can track some objects by camera with servo motor.**

# Dependencies

1. ros2 foxy

2. Arduino DUE

3. micro-ROS

4. CAMERA : Logitech C920 HD PRO**

6. MOTOR  : 360 degree Continuous Rotation Servo Motor**

# References

**1. Camera Launcher**

You can refer to following browser.

**<https://github.com/ros-drivers/usb_cam>**

**2. micro-ROS package**

You can refer to following browser.

**<https://github.com/micro-ROS/micro_ros_arduino>**

You can utilize the example codes(C languages, Arduino) stored in this package.

# How launch this argorithm?
    ros2 run usb_cam usb_cam_node_exe --ros-args --params-file/home/sun/ros2_ws/src/usb_cam-ros2/config/params_1.yaml
    ros2 launch camera_tracking camera_tracking_launch.py

![image](https://github.com/gabrielsunhyuck/object-tracking-usbcam/assets/163500499/e969d7ad-a5ed-4a43-8968-625435805cdd) **!!**

- You should modify the parameters of yalm file stored in camera package. [params_1.yaml]


- 





