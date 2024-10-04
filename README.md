# Human Following Robot

## Overview
This project involves building a **Human Following Robot** using an ultrasonic sensor, a motor driver, and a microcontroller (e.g., Arduino or ESP32). The robot autonomously follows a person by detecting their distance and direction using a camera. This project is great for learning about computer vision, motor control, and autonomous movement systems.

---

## Features
- Follows a human target.
- Controls two DC motors for robot movement.
- Stops or changes direction when the human moves out of range.
- Simple and efficient design for educational purposes.

---

## Components
- **Arduino/ESP32**: Microcontroller to control the robot.
- **Motor Driver (L298N)**: Controls the motors based on commands from the microcontroller.
- **DC Motors (x2)**: Drive the robot forward, backward, or turn.
- **Chassis**: Base to mount the components.
- **Power Supply**: Battery pack for the motors and the controller.
  
---

## Circuit Diagram
- **Motor Driver (L298N)**:
  - Input Pins: Connect to the digital pins on the microcontroller.
  - Output Pins: Connect to the motors.
  - Power: Connect to the power supply.
  
---

## How It Works
1. The ultrasonic sensor detects the distance between the robot and the target (human).
2. If the distance is within a specified range, the microcontroller commands the motor driver to move the robot forward.
3. If the target moves out of range or too close, the robot either stops or adjusts its speed and direction.
4. The robot continuously adjusts its movement based on the real-time distance data.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/human-following-robot.git
cd human-following-robot
```

### 2. Hardware Setup
- Assemble the components as per the circuit diagram.
- Ensure that the connections are firm and accurate.

### 3. Software Setup
- Install the **Arduino IDE** from the [Arduino Website](https://www.arduino.cc/en/software).
- Install the required libraries:
  - **Motor Control Library (AFMotor or similar)**
  
### 4. Upload the Code
- Open the arduino code in the Arduino IDE.
- Select the correct **Board** and **Port**.
- Click on the **Upload** button.

---

## Usage
1. Power up the robot using the battery pack.
2. Place the robot on the ground and ensure it has sufficient room to move.
3. The robot will begin to follow the human target automatically when it detects someone in range.
  
---

## Future Improvements
- **Obstacle Avoidance**: Integrate additional sensors to avoid obstacles while following.
- **Camera Integration**: Use a camera and machine learning to improve human detection.
- **Bluetooth/Wi-Fi Control**: Add remote control functionality for manual operation.
  
---

## License
This project is licensed under the Apache 2.0 License. See the `LICENSE` file for more details.
