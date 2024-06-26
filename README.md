# ![image](https://github.com/gabrielsunhyuck/object-tracking-usbcam/assets/163500499/2d905299-a556-482f-b833-5aa2f788e0c9) object-tracking-usbcam

#### **You can track some objects by camera with servo motor.**

## Dependencies

1. ros2 foxy

2. Arduino DUE

3. micro-ROS

4. CAMERA : Logitech C920 HD PRO

6. MOTOR  : 360 degree Continuous Rotation Servo Motor


## References

**1. Camera Launcher**

You can refer to following browser.

**<https://github.com/ros-drivers/usb_cam>**

**2. micro-ROS package**

You can refer to following browser.

**<https://github.com/micro-ROS/micro_ros_arduino>**

You can utilize the example codes(C languages, Arduino) stored in this package.

## Setting Arduino

1. connecting Arduino DUE or other available boards to your main PC

2. upload the code((Location : /home/<your_workspace>/src/Arduino/camera_tracking/CameraTracking_servo_control4.ino) to Arduino connected with your main PC

3. Launch micro-ROS

## How launch micro-ROS
    cd <your_workspace>
    source ~/<your_workspace>/install/setup.bash
    ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0

## How launch this argorithm?
    ros2 run usb_cam usb_cam_node_exe --ros-args --params-file/home/sun/ros2_ws/src/usb_cam-ros2/config/params_1.yaml
    ros2 launch camera_tracking camera_tracking_launch.py


## Considerations (process in detail)

##### Step 1. Modifying parameter(1)
- You should modify the parameters of yalm file stored in camera package. [params_1.yaml]

- Important information to look at in the yaml file is **video_device**, **frame_id**, and **camera_name**. ![image](https://github.com/gabrielsunhyuck/object-tracking-usbcam/assets/163500499/2ce6474d-7b8a-4027-a0d6-9761a12e763e) 
---
##### Step 2. Modifying parameter(2)
- Then, you have to modify the parameters of node file stored in camera package. [usb_cam_node.cpp]

- You should modify the information of **"camera name"**, **"frame_id"**![image](https://github.com/gabrielsunhyuck/object-tracking-usbcam/assets/163500499/5cf8a66d-4daa-4f5f-96aa-993ca76d8d74)
---
##### Step 3. Working Camera

    sudo chmod 777 /dev/videl*
    cd <your_workspace>
    source ~/<your_workspace>/install/setup.bash
    ros2 run usb_cam usb_cam_node_exe --ros-args --params-file/path/to/ros2_ws/src/usb_cam_config/params_1.yaml
---
##### Step 4. Launching Argorithm

have to open other terminal

    cd <your_workspace>
    source ~/<your_workspace>/install/setup.bash
    ros2 launch camera_tracking camera_tracking.launch.py


## Result

![New-Project](https://github.com/gabrielsunhyuck/object-tracking-usbcam/assets/163500499/5e1ff32c-5733-4611-8e57-f06826adbed9)

![New-Project5](https://github.com/gabrielsunhyuck/object-tracking-usbcam/assets/163500499/59fc986b-24a7-461b-80b1-6671b5a2e522)







  





