ByByte Nano Package Options
===========================

This page describes the available hardware configurations of the ByByte Nano robot.

Basic Configuration
-------------------

.. .. image:: ../../assets/img/bybyte-nano/basic-configuration.png
.. :alt: Basic Configuration

The minimal configuration includes the core sensors, drive system, and Bluetooth connectivity required for most educational and robotics projects.

**Included hardware:**

* Arduino Nano controller
* Motor driver
* Two DC motors
* Wheels
* Bluetooth communication module

**Built-in sensors and indicators:**

* Line sensors
* Ultrasonic distance sensor (sonar)
* Light sensor
* Infrared remote-control receiver
* Buzzer
* WS2812 RGB LEDs

This configuration provides all essential functionality for line following, obstacle detection, remote control, wireless communication, and basic autonomous robot operation.

Included Components (Main Modules)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Printed circuit board (PCB)
* Arduino Nano module (ATmega328p)
* 5V power supply circuitry
* Motor driver (DRV8834)
* DC motors (2x)
* Wheels and mounting hardware (2x)
* Buzzer (1x)
* RGB LEDs (2x)
* Battery and battery holder (1x)
* Light sensors (1x)
* IR receiver (1x)
* Ultrasonic sonar sensor (1x)
* Line sensors (1x5)
* Bluetooth module (1x)

Features
^^^^^^^^

* Programmed autonomous movement
* Line-following mode
* Obstacle avoidance
* Bluetooth remote control
* Automatic headlights activation in low-light conditions
* Control of WS2812 addressable RGB LEDs
* Audible signal (buzzer)
* Headlights and hazard warning lights control
* Automotive-style turn signal indication during turns
* Infrared (IR) remote control support

Basic + Side Sensors
--------------------

.. .. image:: images/side-sensors-configuration.png
.. :alt: Side Sensors Configuration

Description of the robot with additional side infrared sensors. This configuration is recommended for maze navigation, where detecting walls on both sides of the robot is required. The added functionality includes side IR sensors (IR LEDs and IR phototransistors), an operational amplifier, and several supporting components such as resistors, capacitors, and a transistor.

Included Components
^^^^^^^^^^^^^^^^^^^

* Side infrared distance sensors
* Operational amplifier (op-amp) with socket
* Power control transistor
* Supporting passive components (resistors and capacitors)

Additional Features
^^^^^^^^^^^^^^^^^^^

* Maze navigation as the primary functionality.
* Simple sensor-triggered tasks, such as obstacle detection and reaction.
* Additional exercises focused on reading and processing analog signals.

Basic + Camera
--------------

.. .. image:: images/camera-configuration.png
.. :alt: Camera Configuration

The camera configuration is intended for more advanced lessons involving computer vision and image processing. It can also be used for simple real-time video transmission while the robot is moving.

To use this configuration, a compatible camera module must be purchased separately. We recommend a camera with a 120-degree field of view and a longer ribbon cable to allow flexible mounting. For optimal visibility, the camera should be installed on a dedicated holder positioned slightly above the main chassis, providing a better viewing angle of the robot's surroundings.

Included Components
^^^^^^^^^^^^^^^^^^^

* ESP-CAM module
* Camera module with 120° field of view
* Camera mounting bracket
* Push buttons
* 3.3 V power supply components
* Jumper wires for connection to the Arduino module

Additional Features
^^^^^^^^^^^^^^^^^^^

* Real-time video streaming from the robot camera
* Computer vision lessons and examples:
* Marker detection and recognition
* Lane and road following
* Traffic sign detection
* Object detection and tracking
* Remote robot control over Wi-Fi with live video streaming
* Platform for experimenting with AI and computer vision algorithms
