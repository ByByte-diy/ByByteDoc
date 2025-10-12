Programming
===========

Competition Programming
~~~~~~~~~~~~~~~~~~~~~~~

**Maze Solving:**

* Wall following algorithms
* PID control
* Flood fill algorithm
* Path optimization
* Memory management

**Line Following:**

* PID control
* Speed optimization
* Curve handling
* Junction detection

**Remote Control:**

* Bluetooth control
* IR remote control
* WiFi control (with ESP32-CAM module)
* Path finding algorithms (with ESP32-CAM module)

**Obstacle Avoidance:**

* Ultrasonic measurement
* IMU/Gyroscope orientation sensing
* Optical encoders speed feedback
* PID control
* Position tracking
* Emergency stop


Development Environment
-----------------------

1. Install Arduino IDE 2.0 from `https://www.arduino.cc/en/software`
2. Install libraries via Library Manager:

   - NewPing (ultrasonic)
   - MPU6050 (IMU)
   - Adafruit_SSD1306 (OLED)
   - Encoder (encoders)
   - PID_v1 (PID control)

Board Configuration
-------------------

Tools > Board > Arduino Mega 2560
Tools > Port > [Select your port]


Examples
--------

Motor Encoders (snippet):

.. code-block:: cpp

   #include <Encoder.h>
   Encoder leftEncoder(2, 3);
   Encoder rightEncoder(18, 19);
   void setup() { Serial.begin(115200); }
   void loop() {
     Serial.println(leftEncoder.read());
   }

IMU (snippet):

.. code-block:: cpp

   #include <Wire.h>
   #include <MPU6050.h>
   MPU6050 mpu;
   void setup(){ Serial.begin(115200); Wire.begin(); mpu.initialize(); }
   void loop(){ int16_t ax,ay,az,gx,gy,gz; mpu.getMotion6(&ax,&ay,&az,&gx,&gy,&gz); }


