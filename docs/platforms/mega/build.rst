How to Build
============

.. warning::
   Safety first! Disconnect power before working. Double-check polarity.

Configurations
--------------

Basic kit:

- Arduino Mega 2560
- Motor driver/shield
- 4 × DC motors (with optional encoders)
- Ultrasonic sensors (2–4)
- Line sensor array (5–8)
- Battery holder / BMS
- Chassis and fasteners

Extended kit:

- Everything from basic kit
- IMU/Gyro module
- Bluetooth/Wi‑Fi module
- OLED display
- Extra LEDs and indicators

BOM and Parts List
-------------------

- Arduino Mega 2560 board
- Motor drivers (dual H‑Bridge) or shield
- 4 × DC motors + encoders
- HC‑SR04 sensors (×2–4)
- Line sensor array
- IMU (MPU6050)
- OLED (SSD1306)
- Bluetooth/Wi‑Fi module
- BMS + battery (3S LiPo or 6×AA)
- Wires, connectors, screws, nuts, spacers

Schematics and Modules
----------------------

- Power distribution with BMS
- Motor driver connections
- Sensor buses (I2C/SPI/UART)
- Encoder wiring
- Optional modules (display, camera)

Device Assembly
---------------

Phase 1: Planning

1. Review documentation and schematics
2. Inventory components
3. Prepare workspace and tools

Phase 2: PCB/Shield

1. Inspect PCB/shield
2. Solder components if using DIY PCB
3. Mount Arduino Mega and drivers

Phase 3: Chassis

1. Assemble frame and mounts
2. Install motors and wheels
3. Mount PCB/shield and battery holder

Phase 4: Sensors & Modules

1. Mount ultrasonics, line array, IMU
2. Add communication modules and OLED
3. Route cables and secure

Phase 5: Wiring

1. Distribute power rails
2. Wire drivers, sensors, encoders
3. Cable management and labeling

Phase 6: Testing

1. Continuity and polarity checks
2. Power‑on without load
3. Module‑by‑module tests
4. Calibration


