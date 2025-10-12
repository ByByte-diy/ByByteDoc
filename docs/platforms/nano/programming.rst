Programming
===========

Getting Started
~~~~~~~~~~~~~~~

**1. Install Arduino IDE**

Download from: https://www.arduino.cc/en/software

**2. Install Required Libraries**

.. code-block:: bash

   # Open Arduino IDE
   # Go to: Tools > Manage Libraries
   # Search and install:
   - NewPing (for ultrasonic sensor)
   - AFMotor or L298N library (for motors)

**3. Select Board**

.. code-block:: text

   Tools > Board > Arduino Nano (or Uno)
   Tools > Processor > ATmega328P
   Tools > Port > [Select your port]

Basic Examples
~~~~~~~~~~~~~~

**Example 1: Motor Test**

.. code-block:: cpp

   // Motor pins
   int motor1Pin1 = 2;
   int motor1Pin2 = 3;
   int motor2Pin1 = 4;
   int motor2Pin2 = 5;
   
   void setup() {
     pinMode(motor1Pin1, OUTPUT);
     pinMode(motor1Pin2, OUTPUT);
     pinMode(motor2Pin1, OUTPUT);
     pinMode(motor2Pin2, OUTPUT);
   }
   
   void loop() {
     // Move forward
     digitalWrite(motor1Pin1, HIGH);
     digitalWrite(motor1Pin2, LOW);
     digitalWrite(motor2Pin1, HIGH);
     digitalWrite(motor2Pin2, LOW);
     delay(2000);
     
     // Stop
     digitalWrite(motor1Pin1, LOW);
     digitalWrite(motor1Pin2, LOW);
     digitalWrite(motor2Pin1, LOW);
     digitalWrite(motor2Pin2, LOW);
     delay(1000);
   }

**Example 2: Obstacle Avoidance**

.. code-block:: cpp

   #include <NewPing.h>
   
   #define TRIGGER_PIN  12
   #define ECHO_PIN     11
   #define MAX_DISTANCE 200
   
   NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
   
   void setup() {
     Serial.begin(9600);
     // Initialize motors
   }
   
   void loop() {
     int distance = sonar.ping_cm();
     
     if (distance > 0 && distance < 20) {
       // Obstacle detected - turn
       turnRight();
     } else {
       // No obstacle - move forward
       moveForward();
     }
     
     delay(50);
   }

**Example 3: Line Following**

.. code-block:: cpp

   // Line sensor pins
   int leftSensor = A0;
   int rightSensor = A1;
   
   void setup() {
     pinMode(leftSensor, INPUT);
     pinMode(rightSensor, INPUT);
     // Initialize motors
   }
   
   void loop() {
     int left = digitalRead(leftSensor);
     int right = digitalRead(rightSensor);
     
     if (left == LOW && right == LOW) {
       // On line - move forward
       moveForward();
     } else if (left == HIGH) {
       // Line on left - turn left
       turnLeft();
     } else if (right == HIGH) {
       // Line on right - turn right
       turnRight();
     }
   }