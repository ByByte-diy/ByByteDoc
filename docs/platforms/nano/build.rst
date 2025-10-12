How to Build
============

.. warning::
   Safety first! Always disconnect power before making or changing connections.

Configurations
--------------

Basic (recommended for starters):

- Arduino Nano (ATmega328P)
- DRV8833 motor driver
- 2 × N20 DC gear motors with 45 mm wheels
- HC-SR04 ultrasonic sensor
- 5 × TCRT5000 line sensors
- 6F22 ("Krona") battery holder and 6F22 Li‑ion battery
- Prototyping board (PCB or breadboard)
- MINI‑360 DC buck converter (5V/3.3V)

Extended (connectivity and lights):

- Everything from the basic kit
- ESP32‑CAM (Wi‑Fi/camera)
- Bluetooth module HC‑05/HC‑06/HC‑02
- 2 × WS2812B LEDs (headlights)
- IR receiver VS1838 (remote control)

BOM and Parts List
-------------------

- Arduino Nano board (ATmega328P; old bootloader if needed)
- ESP32‑CAM module (optional)
- Bluetooth module HC‑05/HC‑06/HC‑02 (optional)
- DRV8833 motor driver
- 2 × N20 DC motors (6V, 400–750 RPM) with wheels
- HC‑SR04 ultrasonic sensor
- 5 × TCRT5000 line sensors
- 6F22 battery holder + 6F22 Li‑ion battery
- PCB or breadboard
- MINI‑360 power converter (5V and 3.3V)
- 2 × WS2812B 5 mm LEDs (optional)
- IR receiver VS1838
- IR emitter/photodiode (SFH4545, TEFT4300) — side sensors (optional)
- LDR photoresistor (light sensor)
- Passive piezo buzzer
- Motor mounts, screws, nuts, ball caster
- Resistors, capacitors, diodes — small parts
- Wires and jumpers

Schematics and Modules
----------------------

This section helps you connect modules correctly. Detailed printable schematics will be added as images.

- DRV8833 motor driver: VCC/GND power, outputs to motors M1/M2, control IN1–IN4 from Arduino
- TCRT5000 line sensors: 5V/GND power, digital outputs to Arduino pins
- HC‑SR04 ultrasonic: Trig/Echo to digital pins, 5V/GND power
- Side IR sensors: emitter/receiver to analog pins, resistor dividers if needed
- IR receiver VS1838: output to a digital pin with interrupt support
- Power: 6F22 battery → MINI‑360 (5V, 3.3V) → power rails

.. note::
   Ready-to-use wiring diagrams (PNG/SVG) will be added to ``_static/images`` and linked here.

Device Assembly
---------------

Prerequisites
~~~~~~~~~~~~~

- Tools: soldering iron (minimal), cutters, screwdriver, multimeter
- Skills: basic electronics, minimal soldering, attention to detail

Step-by-Step
~~~~~~~~~~~~

Step 1: Preparation

1. Unpack all components
2. Cross-check with the BOM
3. Read all instructions first

Step 2: Chassis

1. Prepare or assemble the chassis
2. Mount the motors
3. Attach the wheels
4. Install the battery holder and breadboard

Step 3: Motor Driver

1. Place the DRV8833 on the breadboard
2. Connect VCC and GND
3. Connect outputs to the motors
4. Connect control pins to the Arduino

Step 4: Sensors

1. Mount the ultrasonic sensor in front
2. Install the line sensors underneath
3. Wire the sensors

Step 5: Arduino

1. Place the Arduino on the board
2. Wire to the motor driver
3. Wire the sensor inputs
4. Distribute power rails

Step 6: Power

1. Insert the battery
2. Connect the holder
3. Optionally add a power switch
4. Double-check polarity

Step 7: Testing

1. Visual inspection
2. Verify connections
3. Upload a test sketch
4. Test each module
5. Calibrate sensors


