ByByte Nano Assembly Process
============================

Assembly Preparation 🛠️
-----------------------

Before starting assembly, prepare your workspace, tools, and all required components. The workspace should be clean, well organized, and free from unnecessary objects that could interfere with the assembly process. Ensure that the area is well lit and provides enough space to safely handle electronic components and tools.

Verify that all components included in your selected robot configuration are available before beginning assembly. It is also recommended to sort and identify the parts in advance to avoid confusion during the build process.

Inspect all tools before use. Every tool, especially the soldering iron, must be in good working condition and free from visible damage. Do not use defective equipment, damaged cables, or tools with exposed electrical conductors.

.. attention::

  If the robot is being assembled by a child, all necessary safety precautions must be taken. The equipment should be inspected and approved by an adult before use, and an adult must supervise the entire assembly process. Special attention should be given when using soldering equipment, sharp tools, or any device that may cause injury if handled improperly.

Step 1 - Prepare Power⚡
------------------------

Prepare and Configure Power Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before soldering any components onto the PCB, prepare the power supply circuitry. The first component that must be configured is the DC-DC voltage regulator.

Connect the DC-DC regulator to a suitable power source and adjust its output voltage to the required value using the onboard adjustment potentiometer. Verify the output voltage with a multimeter before proceeding.

Once the regulator has been configured and tested, set aside all power-related components for installation in the following assembly steps. This ensures that the power system is ready and correctly adjusted before any other components are soldered onto the board.

Two DC-DC regulator variants can be used with the robot: 

* `Mini-360 <https://components101.com/modules/mini360-dc-dc-buck-converter-module>`_
* `HW-613 <https://ampere-electronics.com/product/hw-613-mini-step-down-module-12-24vdc-to-5vdc-3a>`_ (recommended)
 
The HW-613 is the recommended option because it supports selecting a predefined output voltage using solder jumpers. The Mini-360 requires voltage adjustment by turning a potentiometer. When the robot is used by children, the potentiometer may be accidentally rotated, changing the voltage setting and potentially damaging robot components. If the HW-613 is not available and a Mini-360 is used, the potentiometer should be secured after adjustment, for example with a small drop of suitable adhesive.

.. attention::

  The HW-613 must be configured using its solder jumpers. Note that, by default, the jumper connected to the potentiometer adjustment mode is already closed on the module. This connection must be cut before soldering the jumper corresponding to the desired fixed output voltage.

Configure the Mini-360
^^^^^^^^^^^^^^^^^^^^^^

Connect the battery to the input of the Mini-360 regulator and set the multimeter to DC voltage measurement mode . Measure the output voltage and carefully rotate the potentiometer adjustment screw until the required voltage is reached. For a 5 V supply, adjust the output to approximately 5.1 V. For a 3.3 V supply, the output should be within the range of 3.2–3.4 V. After the regulator has been adjusted and verified, it can be soldered onto the PCB. To prevent accidental changes to the setting during operation, secure the potentiometer with a small drop of glue or lacquer.

.. raw:: html

   <div class="video-embed">
    <iframe
      src="https://www.youtube.com/embed/VdwDSgle6j4"
      title="Mini-360 voltage adjustment"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen>
    </iframe>
   </div>

Configure the HW-613
^^^^^^^^^^^^^^^^^^^^

For the HW-613 regulator, first cut the solder jumper marked ADJ and then solder the jumper corresponding to the required output voltage. Before installing the regulator on the PCB, connect the battery to the regulator input and set the multimeter to DC voltage measurement mode. Measure the output voltage to verify that it is within the allowed range for the selected setting. Only after the output voltage has been confirmed should the regulator be soldered onto the PCB.

.. raw:: html

   <div class="video-embed">
    <iframe
      src="https://www.youtube.com/embed/MiNVErTYu5o"
      title="HW-613 voltage adjustment"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen>
    </iframe>
   </div>
   

After the regulators have been configured and verified, solder the power supply components onto the PCB according to the selected robot configuration.

The 5 V power supply is mandatory for all ByByte Nano configurations and must always be installed. Solder the 5 V DC-DC regulator together with all associated power-supply components, including capacitors, filters, and any other parts required by the 5 V circuit. Verify that all solder joints are clean and properly formed before proceeding.

.. raw:: html

   <div class="video-embed">
    <iframe
      src="https://www.youtube.com/embed/umG7YM0Vad8"
      title="Power supply components soldering"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen>
    </iframe>
   </div>

The 3.3 V power supply is optional and is only required when assembling a robot configuration that includes the camera module. If the camera is not used, the entire 3.3 V power-supply circuit may be omitted, including the regulator, capacitors, filters, and other associated components. For camera-equipped configurations, solder all components of the 3.3 V power-supply circuit into their designated positions on the PCB and inspect all connections before continuing.

.. raw:: html

   <div class="video-embed">
    <iframe
      src="https://www.youtube.com/embed/T0ZU_tptmJQ"
      title="3.3 V power supply components soldering"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen>
    </iframe>
   </div>

After soldering the regulators, visually inspect the board for solder bridges, cold joints, or incorrectly installed components. Pay particular attention to the regulator orientation and polarity markings. If available, use a multimeter in continuity mode to verify that there is no short circuit between the power rails before proceeding to the next assembly step.

After the inspection, connect the battery and verify all power rails with a multimeter. Check that each regulator provides the expected output voltage and that power is correctly distributed throughout the board. 

.. attention::

  Do not continue the assembly process until all supply voltages have been measured and confirmed to be within their expected ranges.

Step 2 - Side IR Sensors ⚡
---------------------------

Mount and Test Side Obstacle Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This step applies only if you are building the **Basic + Side Sensors** configuration. If your robot does not include side infrared obstacle sensors, skip this step and continue with Step 3.

If you plan to use the side IR sensors, mount them next and verify that the circuit works correctly before continuing the assembly. Prepare the required components and tools in advance.

Mount Components on the Main PCB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Start with resistors** 🔍

   Solder the resistor components onto the main PCB first.

#. **Install the op-amp socket, control transistor, and ceramic capacitors** 🔍

   After the resistors, solder the op-amp socket, the control transistor, and the ceramic capacitors.

#. **Prepare and mount the IR phototransistors** 🔍

   Before soldering, wrap each IR phototransistor in black heat-shrink tubing with a diameter of about 6 mm so that the sensor sits in a short tunnel. **Black heat-shrink tubing is required.**

   Solder the IR phototransistors (**TEFT4300**) onto the main PCB. Carefully check the pin markings on the PCB and compare them with the pinout shown in the component  `datasheet <https://www.vishay.com/docs/81549/teft4300.pdf>`_.

   .. image:: ../_static/img/teft4300-wrap.png
      :alt: TEFT4300 wrapped in black heat-shrink tubing
      :align: center

   .. attention::

      If the IR receiver orientation is incorrect, the side-sensor circuit will not work.

#. **Prepare the IR LED boards** 🔍

   When all components on the main PCB are in place, move on to the IR LEDs (**SFH4545**). They are mounted on separate small boards that are separated from the panel with pliers. Trim or file any sharp edges left from the breakaway tabs.

#. **Prepare and solder the IR LEDs** 🔍

   Wrap each IR LED in black heat-shrink tubing so that only the narrow front tip remains visible. Only after this preparation, solder the LED onto the auxiliary board. Pay close attention to the pin orientation. On the `SFH4545 pdf <https://look.ams-osram.com/m/3456970c8eccd2cb/original/SFH-4545.pdf>`_, the **longer lead is the cathode (negative)**.

   .. image:: ../_static/img/sfh4545-wrap.png
      :alt: SFH4545 wrapped in black heat-shrink tubing
      :align: center

#. **Install the vertical IR sensor assemblies** 🔍

   Mount the completed IR sensor assemblies vertically ongto the main PCB using 90-degree pin headers.

#. **Install the op-amp and prepare for testing** 🔍

   When all parts are soldered in place, install the operational amplifier in its socket. The side-sensor circuit is now ready for a functionality test.

Test the Side-Sensor Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will need a multimeter, a battery with PP3/Krona-style leads, and a jumper wire (a short piece of tinned wire).

#. **Connect the power supply** 🔋

   Connect the battery and set the multimeter to DC voltage measurement mode.

#. **Verify op-amp supply voltage** 🔍

   Turn on the power switch and measure the voltage on the op-amp power pins (pins 4 and 8). You should read **5 V**. If the voltage is present, continue to the next check.

#. **Measure the op-amp outputs with the IR LEDs off** 🔍

   Measure the voltage on the op-amp outputs (pins 1 and 7). With the IR LEDs off, the output voltage should be low, up to about **1 V**. If this is correct, continue.

#. **Enable the IR LEDs and verify sensor response** 🔍

   Turn the IR LEDs on by applying a **5 V** control signal to the driver transistor input. Use a jumper wire to connect **5 V** (Arduino 5 V rail) to **D4** on the PCB.

   You can use a phone camera to confirm that the IR LEDs are on, because many cameras can detect infrared light.

   Measure the voltage on the op-amp outputs (pins 1 and 7) again. The voltage should now increase when an obstacle is moved closer to the sensor. The closer the obstacle, the higher the voltage. At maximum proximity, the level should reach about **3.8 V**.

#. **Confirm both channels** ✅

   Verify that both outputs respond correctly (**pin 1 — left sensor**, **pin 7 — right sensor**). If both channels behave as expected, the side sensors are working and you can continue with the robot assembly.

If something does not work, go to the :doc:`Troubleshooting <bybyte-nano-troubleshooting>` section. Before assembly, review the video instructions for this step.

Step 3 - Solder Small Components⚡
----------------------------------

Solder Small Components and Basic Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Begin by soldering all low-profile through-hole components, including resistors, diodes, capacitors, and other small passive parts. Installing these components first makes the remaining assembly steps easier and provides better access to the PCB.

Next, solder the basic sensors used in all robot configurations:

* Light sensor
* IR receiver

After completing this step, inspect all solder joints and verify component orientation before proceeding.

Step 4 - Connectors and Motors⚡
--------------------------------

Solder Connectors and Install Motors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this stage, solder all connectors on the main PCB according to the board markings.

Next, separate the motor adapter boards from the panel and solder the corresponding connectors onto each adapter. After that, solder the adapter boards directly to the N20 motors. Repeat this process for both motors.

Once both motor adapters are soldered to the motors and all connectors are installed on the main PCB, proceed with motor installation.

The motors are mounted using dedicated plastic brackets designed for N20 motors. Secure each motor in its bracket and attach the assembly to the main PCB.

.. note::

  When mounting the motors, the screw head must be located on the underside of the PCB. The nut is inserted from the top into the dedicated slot in the plastic bracket. This prevents the nut from rotating during assembly and makes installation easier.

Step 5 - Install Sensors⚡
--------------------------

Install and Solder the Ultrasonic Sensor and Line Tracker Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Begin with the ultrasonic sensor mounted at the front of the PCB. Before soldering, measure the required pin length and trim the leads as close to the PCB as possible. The sensor pins should not protrude below the board, so keep the exposed leads to a minimum. During soldering, ensure that the solder joint provides sufficient mechanical support from the component side of the PCB. Large solder pads are provided specifically for this purpose.

After soldering, any remaining pin protrusions should be minimal, as clearance is required for the line tracker connector installed nearby.

Next, install the line tracker connector. This connector is mounted from the bottom side of the PCB (solder side) and soldered from the top side (component side).

Once the connector is installed, attach the line tracker sensor module. The PCB includes dedicated mounting tabs for this purpose. Secure the module using M3 screws and locking nuts. To maintain the correct spacing between the boards, use 5 mm plastic spacers.

After the ultrasonic sensor, line tracker module, Arduino controller, and all remaining modules are installed and secured in place, proceed to the next assembly step.

Step 6 - Wheels and Battery Holder⚡
------------------------------------

Install Roller Wheels and Battery Holder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now it is time to install the roller wheels and the battery holder.

First, install the roller wheels. This step must be completed before mounting the battery holder, because once the holder is fixed in place, access to the roller wheel mounting holes will be blocked.

Before installation, remove the screws from each roller wheel assembly.

.. attention::

  Be careful: inside the wheel assembly there are several small balls and one larger ball. When removing the screws, the assembly may come apart and there is a risk of losing these parts. Disassemble the wheel carefully and avoid pressing on the main roller.

To mount the roller wheels:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Insert the removed screws through the PCB from the component side (see the markings on the board).
Position the roller wheel on the underside of the PCB.
Tighten the screws until the wheel is firmly secured and does not wobble.

Repeat the same procedure for the second roller wheel.

Mount the Battery Holder
^^^^^^^^^^^^^^^^^^^^^^^^

Once both wheels are installed, proceed with mounting the battery holder.

A battery holder with pre-attached wires is recommended. Measure the required wire length, cut off any excess, strip and tin the wire ends, then solder them to the designated pads on the PCB.

Secure the battery holder using M2 screws and self-locking nuts.

Congratulations! Your robot is almost ready for operation.

Step 7 - Bluetooth and Battery⚡
--------------------------------

Install Bluetooth Module and Battery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The final assembly stage is installing the Bluetooth module and connecting the battery.

The Bluetooth module is mounted directly onto the PCB using 90-degree angled pin headers. In most cases, these headers are already soldered to the module. If your module has a 6-pin header installed, remove the two outer pins, as only four connections are required: power and data lines.

Position the module according to the markings on the main PCB. The module should sit flush against the board without any gap between the Bluetooth module and the PCB. Once properly aligned, solder all four pins and trim any excess leads.

After soldering, verify that the module is firmly attached and does not move.

.. note::

  Avoid mounting the module at a distance from the PCB, as this makes it more vulnerable to mechanical damage and causes it to protrude unnecessarily.

With the Bluetooth module installed, perform one final visual inspection of all solder joints and components. Check that there are no solder bridges, loose connections, or incorrectly installed parts.

The hardware assembly is now complete.

Step 8 - Initial Inspection⚡
-----------------------------

Before powering the robot for the first time, carefully inspect all solder joints, connectors, and wiring. Verify that all components are installed in the correct orientation and that there are no accidental shorts between adjacent pads or traces.

Perform a final visual inspection of the assembled robot:

* Check all soldered connections.
* Verify motor wiring polarity.
* Confirm that sensors and modules are firmly connected.
* Ensure that no loose wires can interfere with moving parts.
* Check that the battery connection is correct.

Correct any issues before proceeding.

Step 9 - Firmware Upload⚡
--------------------------

The robot is now ready for firmware installation.

Connect the controller to your computer and upload the test sketch or the desired firmware version. For testing, upload the maintenance and diagnostics sketch that verifies all robot functions and is intended specifically for repair and servicing procedures. Detailed instructions are provided in the Firmware section.

Step 10 - Functional Test⚡
---------------------------

After uploading the firmware, perform a complete functional test of the robot.

.. warning::

  If the controller already contains previously installed firmware, the robot may begin moving immediately after power is applied.

Before switching on the robot, make sure the wheels do not touch the table or any other surface. Place the robot on a stand, hold it securely, or otherwise prevent unintended movement to avoid the robot "escaping" during testing.

**Verify the operation of:**

* Power system
* Motors
* Line sensors
* Distance sensors
* LEDs and indicators
* Communication modules
* Additional optional hardware

If any problems are detected, disconnect power, identify the cause, and correct the issue before continuing. Once all tests pass successfully, the robot is ready for normal operation and further software development.