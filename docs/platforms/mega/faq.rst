Frequently Asked Questions
==========================

Assembly Questions
~~~~~~~~~~~~~~~~~~

**Q: Do I need to solder anything?**

A: The platform comes pre-assembled with all components soldered. No soldering required for basic operation.

**Q: How long does assembly take?**

A: Assemble in 6-8 hours. It's not a difficult task, but you need to be careful with the components.

**Q: Can I use different motors?**

A: The platform uses G16 motors (12V, 400-750 RPM). You can replace with similar 12V DC motors, but you'll need to adjust mounting and code.

**Q: Can I add more sensors?**

A: Yes! You have 17 free digital pins and 6 free analog pins for additional sensors. Use I2C for multiple devices.

**Q: Is the platform modular?**

A: Yes, the design allows for easy sensor addition and customization while maintaining core functionality.

Component Questions
~~~~~~~~~~~~~~~~~~~

**Q: Arduino Mega or other boards?**

A: The platform is designed specifically for Arduino Mega 2560 (ATmega2560). May use chip ATmega1280 with arduino bootloader. (It`s not tested`)

**Q: What battery should I use?**

A: 1S Li-ion 18650 battery (3.7V-4.2V, 2200+ mAh recommended). The platform includes battery protection and charging circuit.

**Q: Can I use a different battery?**

A: The platform is designed for 18650 Li-ion batteries. Using other 3.7v battery types may require modifications battery holder.

**Q: Why does the charging IC get hot?**

A: The TP4056 charging IC can get warm during charging (especially at 1A current). This is normal - ensure proper ventilation and don't touch the PCB during charging.

**Q: Can I charge while using the robot?**

A: No, charging is only possible when the device is powered off. This protects the battery and charging circuit.

**Q: What's the maximum load capacity?**

A: Tested with more than 2000g load using 750 RPM motors. The platform is designed for heavy-duty applications.

Programming Questions
~~~~~~~~~~~~~~~~~~~~~

**Q: Which IDE should I use?**

A: Arduino IDE 2.0 (recommended) or Arduino IDE 1.8.x. Also compatible with PlatformIO. You can use VS Code with Arduino or PlatformIO extensions.

**Q: How do I program the robot?**

A: Connect via USB-C port, select Arduino Mega 2560 board and port, and upload your code. The platform includes USB-UART module for programming.

**Q: Where do I find example code?**

A: You can use Arduino IDE with our library and examples. Also you can use PlatformIO with our library and examples.

**Q: How do I use the sensors?**

A: Most sensors are always on (ultrasonic, IMU, encoders). Some are program switchable (line sensors, IR side sensors, Bluetooth). Check the specification for details.

**Q: Can I use Python?**

A: Yes, via serial communication with a computer or using MicroPython on an ESP32-CAM module (optional). You can run the code on you PC and communicate with the robot via bluetooth serial.

**Q: How do I implement PID control?**

A: Use the PID library. The platform includes optical encoders for feedback control. Example code available in our repository.

**Q: My code won't upload, what's wrong?**

A: Check: Correct board selected (Arduino Mega 2560), correct port, USB-C cable connected, device powered on. You must be use an USB data cable for programming.

Performance Questions
~~~~~~~~~~~~~~~~~~~~~

**Q: How long does the battery last?**

A: 1-3 hours typical use, depending on motor usage and sensor activity. The platform includes battery voltage monitoring.

**Q: What's the maximum speed?**

A: Depends on motors and load. With G16 motors (750 RPM): up to 1.77 m/s (6km/h) on smooth surfaces.

**Q: How accurate is line following?**

A: With 6 analog sensors: ±10-20mm accuracy.

**Q: Can it handle slopes?**

A: Yes, the platform can handle moderate slopes. Performance depends on load and motor power.

**Q: What's the range of ultrasonic sensors?**

A: HC-SR04 sensors have 2-70cm (effective) range with ±3mm accuracy. Always on for continuous obstacle detection.


Support & Resources
~~~~~~~~~~~~~~~~~~~

**Q: Where can I get help?**

A: Check our GitHub discussions, community channels and social, or contact support. Advanced documentation available for competition programming.

**Q: Are there video tutorials?**

A: Yes, comprehensive video tutorials available covering assembly, programming, and advanced features.

**Q: Can I get spare parts?**

A: Yes, all components are available as spare parts. Contact us for specific requirements.

**Q: Is there a warranty?**

A: The project is provided as is, and the authors are not responsible for equipment damage or other issues related to improper use, assembly, or low-quality components.
