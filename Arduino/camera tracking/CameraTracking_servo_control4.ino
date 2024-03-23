#include <micro_ros_arduino.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <std_msgs/msg/float32.h>

#include <Servo.h>  // Use ServoDuo library for Duo board

rcl_subscription_t subscriber;
std_msgs__msg__Float32 pwm_msg;
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;

Servo servo;  // Use ServoDuo for Duo board

#define PWM_PIN 9 // Change this to the actual PWM pin connected to your servo
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}

void error_loop() {
  while (1) {
    delay(1); // default 100
  }
}

void subscription_callback(const void *msgin) {
  const std_msgs__msg__Float32 *msg = (const std_msgs__msg__Float32 *)msgin;

  // Print received PWM value to Serial Monitor
  Serial.print("Received PWM: ");
  Serial.println(msg->data);

  // Assuming the PWM range for the servo is 0 to 180
  int pwm_value = static_cast<int>(msg->data);
  pwm_value = constrain(pwm_value, 0, 180);

  // Map the PWM value to the servo motor's range (adjust if needed)
  int servo_value;

  // Modify the servo position based on the mapped value
  // Adjust these conditions based on your servo's behavior
  if (pwm_value == 90) {
    // Rotate clockwise (adjust the angle as needed)
    servo_value = 90;  // or any other angle

  } else {
    // Adjust servo value based on conditions
    if (pwm_value < 90) {
      servo_value = static_cast<int>(90 - (pwm_value * 0.5));
    } else {
      servo_value = static_cast<int>((pwm_value * 0.5) + 90);
    }
  }

  // Set the servo position based on the modified value
  servo.write(servo_value);
  
}

void setup() {
  set_microros_transports();

  // Initialize Serial Monitor
  Serial.begin(115200);

  servo.attach(PWM_PIN);

  allocator = rcl_get_default_allocator();

  // Create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // Create node
  RCCHECK(rclc_node_init_default(&node, "micro_ros_arduino_node", "", &support));

  // Create subscriber
  RCCHECK(rclc_subscription_init_default(
      &subscriber,
      &node,
      ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32),
      "motor_control"));

  // Create executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 1, &allocator));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &pwm_msg, &subscription_callback, ON_NEW_DATA));
}

void loop() {
  delay(1);
  RCCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(10))); // default : 100
}