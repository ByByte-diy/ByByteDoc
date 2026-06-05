ByByte Nano Package Options
===========================

This page describes the available hardware configurations of the ByByte Nano robot.

Basic Configuration
--------------------

.. .. image:: ../../assets/img/bybyte-nano/basic-configuration.png
.. :alt: Basic Configuration

The minimal configuration includes the core sensors, drive system, and Bluetooth connectivity required for most educational and robotics projects.

Included hardware:

* Arduino Nano controller
* Motor driver
* Two DC motors
* Wheels
* Bluetooth communication module

Built-in sensors and indicators:

* Line sensors
* Ultrasonic distance sensor (sonar)
* Light sensor
* Infrared remote-control receiver
* Buzzer
* WS2812 RGB LEDs

This configuration provides all essential functionality for line following, obstacle detection, remote control, wireless communication, and basic autonomous robot operation.

Included Components
^^^^^^^^^^^^^^^^^^^

* TODO

Features
^^^^^^^^

* TODO

Basic + Side Sensors
--------------------

.. .. image:: images/side-sensors-configuration.png
.. :alt: Side Sensors Configuration

Description of the robot with additional side infrared sensors. This configuration is recommended for maze navigation, where detecting walls on both sides of the robot is required. The added functionality includes side IR sensors (IR LEDs and IR phototransistors), an operational amplifier, and several supporting components such as resistors, capacitors, and a transistor.

Included Components
^^^^^^^^^^^^^^^^^^^

* TODO

Additional Features
^^^^^^^^^^^^^^^^^^^

* TODO

Basic + Camera
--------------

.. .. image:: images/camera-configuration.png
.. :alt: Camera Configuration

The camera configuration is intended for more advanced lessons involving computer vision and image processing. It can also be used for simple real-time video transmission while the robot is moving.

To use this configuration, a compatible camera module must be purchased separately. We recommend a camera with a 120-degree field of view and a longer ribbon cable to allow flexible mounting. For optimal visibility, the camera should be installed on a dedicated holder positioned slightly above the main chassis, providing a better viewing angle of the robot's surroundings.

Included Components
^^^^^^^^^^^^^^^^^^^

* TODO

Additional Features
^^^^^^^^^^^^^^^^^^^

* TODO
