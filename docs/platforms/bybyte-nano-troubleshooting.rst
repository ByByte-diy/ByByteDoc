ByByte Nano Troubleshooting
===========================

Power supply issues 🔌
-----------------------

Power LED does not light up after enabling the power switch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Symptoms**:

* The 5 V power circuit has been soldered.
* The power source is connected.
* The power switch is turned on.
* The power indicator LED remains off.
* No 5 V power is present on the board.

**Possible causes and checks:**

1. **Check the power source** 🔋

   Verify that the battery or external power supply is charged and connected correctly. Measure the voltage directly at the power input connector.

2. **Inspect solder joints** 🔍

   Carefully inspect all solder joints in the 5 V power circuit. Cold solder joints, solder bridges, or unsoldered pins may interrupt power delivery.

3. **Verify component orientation** 🔍

   Check that all polarized components are installed correctly:

   * Voltage regulator
   * Protection diode
   * Electrolytic capacitors
   * Power indicator LED

4. **Check the power switch** 🔍

   Use a multimeter in continuity mode to verify that the switch closes the circuit when turned on.

5. **Measure voltage step by step** 🔍

   Follow the power path with a multimeter:

   * Power input connector
   * Before the power switch
   * After the power switch
   * Regulator input
   * Regulator output (5 V rail)

   The point where voltage disappears usually indicates the location of the fault.

6. **Check for short circuits** ⚡

   With power disconnected, measure the resistance between the 5 V rail and GND. A very low resistance may indicate a solder bridge or incorrectly installed component.

**Expected result:**

After correcting the issue, the power indicator LED should illuminate when the switch is turned on, and a stable 5 V supply should be present on the board.

.. note::
    When assembling a configuration that includes the optional 3.3 V power rail, the assembly and verification procedure is almost identical to the 5 V rail. The main difference is that the 3.3 V circuit does not include a power indicator LED or the protection diode used in the 5 V supply path. Apart from these omitted components, install and inspect the regulator, capacitors, filters, and all other associated parts in the same manner as described for the 5 V power supply. Verify the output voltage after assembly and confirm that the 3.3 V rail is free of shorts before continuing.

Motor issues 🔄
----------------

Motors do not move after uploading the test firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Symptoms:**

* The robot powers on normally.
* The controller is programmed successfully.
* The test firmware starts running.
* The motors do not rotate, or only one motor rotates.

**Possible causes and checks:**

1. **Check motor solder joints** 🔍

   Inspect the solder joints between the motor terminals and the motor adapter boards. Poor solder joints or broken connections can prevent power from reaching the motors.

   Gently pull on the wires or adapter board and verify that the connection is mechanically secure.

2. **Check motor driver solder joints** 🔍

   Carefully inspect all solder joints associated with the motor driver socket and surrounding components. Look for:

   * Cold solder joints
   * Unsoldered pins
   * Solder bridges between adjacent pins

3. **Verify motor driver installation** 🔍

   Ensure that the motor driver module is inserted into the socket in the correct orientation.

   Installing the driver backwards may prevent operation and can potentially damage the module.

   Compare the driver orientation with the PCB markings and assembly photographs.

4. **Check motor driver power** 🔍

   Most motor driver modules include a power indicator LED.

   * Turn on the robot.
   * Verify that the LED on the motor driver is illuminated.
   * If the LED is off, measure the supply voltage on the driver module.

   If no voltage is present, inspect the power connections between the main PCB and the driver.

5. **Verify motor connector installation** 🔍

   Confirm that both motor connectors are fully inserted and connected to the correct sockets.

   A partially inserted connector may appear connected while making poor electrical contact.

6. **Measure voltage on motor outputs** 🔍

   While the test firmware is commanding the motors to run, measure the voltage on the motor output terminals of the driver.

   If voltage is present but the motor does not rotate, the problem is likely in the motor wiring or the motor itself.
   If no voltage is present, the issue is likely related to the driver, controller signals, or firmware configuration.

7. **Check controller installation** 🔍

   Verify that the Arduino controller is correctly installed in its socket and fully seated.

   Bent pins or poor contact can prevent the motor control signals from reaching the driver.

8. **Verify firmware configuration** 🔍

   Ensure that the correct test firmware was uploaded and that the motor control pins match the hardware revision being assembled.

   If custom firmware is used, verify:

   * Motor enable pins
   * Direction pins
   * PWM outputs

9. **Check battery voltage under load** 🔍

   A weak or discharged battery may provide enough power for the controller but not enough current for the motors.

   Measure the battery voltage while the motors are commanded to run. A significant voltage drop indicates that the battery should be charged or replaced.

10. **Test motors directly** 🔍

    Disconnect the motors from the driver and briefly connect them directly to a suitable power source.

    If a motor does not rotate during this test, the motor or its wiring may be defective.

11. **Check for mechanical blockage** 🔍

    Verify that:

    * Wheels rotate freely.
    * No screws are rubbing against moving parts.
    * Wires are not trapped in the drivetrain.
    * The gearbox is not damaged.

**Expected result:**

When the motor driver receives power and control signals correctly, both motors should rotate during the test program. If only one motor operates, compare the wiring, solder joints, and driver connections of the working side with the non-working side to identify the difference.

.. attention::
    **USB Power and Motor Operation**

    When the robot is powered from the USB connector, the controller, sensors, LEDs, and other low-power electronics can operate even if the main power switch is turned off. This allows firmware upload, debugging, and basic testing without enabling the motor power circuit.

    However, the motors are powered through the switched power path. If the power switch is in the OFF position, the motor driver will not receive motor supply voltage and the motors will not move.

    To operate the motors, the main power switch must be turned ON, regardless of whether the robot is powered from the battery or from USB.

Arduino issues 💻
------------------

Arduino Nano cannot be programmed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Symptoms:**

* The Arduino Nano is connected to a computer using a USB cable.
* The Arduino IDE cannot upload firmware.
* An error message appears during upload.
* The board does not appear in the list of available serial ports.

**Possible causes and checks:**

1. **Check the USB cable** 🔌

   Many USB cables are intended only for charging and do not contain data wires.

   Try a known-good USB data cable and reconnect the board.

2. **Verify USB connection** 🔍

   Ensure that the USB connector is fully inserted into both the computer and the Arduino Nano.

   Inspect the connector for mechanical damage or poor solder joints.

3. **Check that the board powers up** ⚡

   When connected through USB, the power LED on the Arduino Nano should illuminate.

   If no LEDs light up, verify the USB cable and inspect the board for shorts.

4. **Select the correct board** 🔍

   In the Arduino IDE, verify that the correct board type is selected:

   Tools → Board → Arduino Nano

5. **Select the correct processor** 🔍

   Some Nano-compatible boards use the older bootloader.

   If upload fails, try:

   * Tools → Processor → ATmega328P
   * Tools → Processor → ATmega328P (Old Bootloader)

   Test both options if you are unsure which version is installed.

6. **Select the correct serial port** 🔍

   Verify that the correct COM port (Windows) or serial device (Linux/macOS) is selected in the Arduino IDE.

   Disconnect and reconnect the board to identify which port appears.

7. **Install USB drivers** 💻

   Many Nano-compatible boards use the CH340 USB-to-serial converter.

   If the board is not detected by the operating system, install the appropriate USB driver and reconnect the board.

8. **Check for shorts on RX and TX pins** 🔍

   Devices connected to pins D0 (RX) and D1 (TX) can interfere with programming.

   Disconnect any external modules connected to these pins and try uploading again.

   If an ESP-CAM module is installed, verify the communication switch settings. When the switches are configured for communication with the camera, they may interfere with uploading firmware to the Arduino Nano.

9. **Inspect solder joints and headers** 🔍

   If the Nano is installed in sockets, verify that all pins are correctly aligned and fully inserted.

   Look for bent pins, solder bridges, or damaged traces.

10. **Try manual reset during upload** 🔍

    Start the upload process and briefly press the RESET button when the IDE displays the upload message.

11. **Test with a simple sketch** 🔍

    Upload the standard Blink example.

    If Blink uploads successfully, the programming interface is working correctly and the issue may be related to the firmware being uploaded.

**Expected result:**

After correcting the issue, the Arduino Nano should be detected by the computer, appear as a serial port, and accept firmware uploads without errors.

Line Sensor Problems 📉
------------------------

**Symptoms:**

* The robot does not detect the line at all.
* One or more sensors always report the same state.
* The robot detects the line inconsistently.
* All sensors appear permanently active regardless of the surface color.
* Line following works on one track but fails on another.

**Possible causes and checks:**

1. **Check connector installation** 🔍

   Verify that the line sensor connector is soldered correctly and that all pins have reliable electrical contact.

   Inspect for:

   * Cold solder joints
   * Unsoldered pins
   * Solder bridges between adjacent pins

2. **Verify sensor module orientation** 🔍

   Ensure that the line sensor module is mounted in the correct orientation and connected to the proper connector.

   Incorrect installation may swap sensor outputs or prevent operation entirely.

3. **Check mounting height** 🔍

   The distance between the sensor module and the surface is critical.

   Verify that:

   * The specified spacers are installed.
   * The module is parallel to the floor.
   * The sensor is not tilted.

   Excessive distance may reduce sensitivity, while insufficient distance may cause unreliable readings.

4. **Inspect the sensor module** 🔍

   Examine the module for damaged components, cracked solder joints, or contamination on the infrared LEDs and phototransistors.

   Dust, glue residue, fingerprints, or scratches can affect performance.

5. **Verify power supply** 🔍

   Measure the supply voltage on the sensor module.

   Ensure that the module receives the expected voltage and that GND is connected correctly.

6. **Test individual sensor outputs** 🔍

   Using a multimeter or diagnostic firmware, verify that each sensor changes state when moved between a dark line and a light background.

   If only one channel fails, the problem is likely localized to that sensor element or its associated circuitry.

7. **Check the track material** 🔍

   Different materials reflect infrared light differently.

   A line that appears visually black may still reflect significant infrared light, while some colored materials may absorb infrared radiation effectively.

   Always test the robot on the actual track material intended for use.

8. **Sensor module is too sensitive** 🔍

   This is a common issue with inexpensive line sensor modules.

   Some modules are configured with very high infrared LED current and may report line detection continuously, regardless of whether the sensor is positioned over a dark or light surface.

   Typical symptoms include:

   * All sensors always active.
   * Little or no difference between black and white surfaces.
   * Reliable operation only at unusually large distances from the floor.

9. **Reduce infrared LED current** 🔍

   If the sensor module is excessively sensitive, the infrared LED current should be reduced.

   On many commonly available modules, each sensor channel contains an SMD resistor in series with the infrared LED. These resistors are often marked 221 (220 Ω).

   *To reduce sensitivity:*

   Replace the five 220 Ω resistors with higher-value resistors.
   Typical replacement values are between 1 kΩ and 2 kΩ.
   The optimal value depends on the track material, ambient lighting conditions, and required detection distance.

   This modification requires desoldering and replacing all five SMD resistors on the module.

   After replacement, test the sensor on the intended track and adjust the resistor value if necessary.

10. **Ambient light interference** 🔍

   Strong sunlight or intense infrared sources may affect sensor readings.

   Test the robot indoors or under controlled lighting conditions to determine whether ambient light is contributing to the problem.

**Expected result:**

Each sensor should clearly distinguish between the line and the surrounding surface. Sensor outputs should change reliably when moving between dark and light areas, and the robot should be able to follow the track consistently.

.. note::

   The currently supported line sensor modules are commercially available third-party products. Their characteristics may vary significantly between manufacturers and production batches.

   Future revisions of the ByByte Nano platform are planned to include custom-designed line sensor modules with improved consistency, optimized sensitivity, and better suitability for educational robotics applications.

Buzzer does not work 🔊
-----------------------

**Symptoms:**

* The robot powers on normally.
* Firmware is running.
* No sound is produced by the buzzer.

**Possible causes and checks:**

1. Verify that the buzzer is installed in the correct orientation.
2. Inspect the buzzer solder joints for cold joints or missing connections.
3. Check continuity between the buzzer pins and the controller. Verify that the transistor controlling the buzzer is installed in the correct position and orientation, and confirm that its component value matches the schematic.
4. Confirm that the firmware actually enables the buzzer output.
5. Measure the voltage on the buzzer pins while a sound should be playing.

**Expected result:**

The buzzer should produce an audible tone when activated by the firmware.

Light Sensor Problems 💡
-------------------------

**Symptoms:**

* The robot always reports the same light level.
* Light measurements do not change when illumination changes.
* Readings are unstable or excessively noisy.

**Possible causes and checks:**

1. Verify that the light sensor is installed in the correct orientation.
2. Inspect all solder joints associated with the sensor and its supporting components.
3. Check that the sensor receives the correct supply voltage.
4. Measure the sensor output while changing the light level. The voltage should change accordingly.
5. Ensure that the firmware is configured to use the correct analog input pin.

**Expected result:**

The reported light level should change smoothly when the sensor is exposed to different lighting conditions.

IR Receiver Problems 📡
-----------------------

**Symptoms:**

* The robot does not respond to the remote control.
* Only some button presses are detected.
* Reception distance is very short.

**Possible causes and checks:**

1. Verify that the IR receiver is installed in the correct orientation.
2. Inspect the solder joints and confirm that all receiver pins are connected properly.
3. Check that the receiver receives the correct supply voltage.
4. Confirm that the remote control battery is charged.
5. Ensure that the firmware is configured for the correct IR receiver pin and protocol.
6. Avoid direct sunlight or strong infrared light sources during testing, as they may interfere with reception.

**Expected result:**

The robot should reliably detect commands from a compatible IR remote control at normal operating distances.

