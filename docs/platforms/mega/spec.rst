Technical Specifications
========================

Platform
~~~~~~~~

* **Microcontroller:** ATmega2560
* **Output Voltage:** 3.3V, 5V, 12V (switchable)
* **Input Voltage:** 3.7V - 4.2V (1S Li-ion battery 18650)
* **Digital I/O Pins:** 17 (free)
* **Analog Input Pins:** 6 (free)
* **Flash Memory:** 256 KB
* **SRAM:** 8 KB
* **EEPROM:** 4 KB
* **Clock Speed:** 16 MHz
* **PWM Pins:** 6

Motors & Movement
~~~~~~~~~~~~~~~~~

* **Motor Type:** DC geared motors G16
* **Voltage:** 12V
* **RPM:** 400-750 (typical)
* **Motor Driver:** Dual H-Bridge TB6612FNG
* **Speed Control:** PWM with feedback
* **Direction Control:** Digital pins
* **Current Protection:** Yes
* **Encoder Resolution:** 12 pulses/rotation (typical)

Included Sensors & Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Ultrasonic distance sensors (HC-SR04, *always on*)
* Line following array (6 analog sensors, *program switchable*)
* IMU/Gyroscope (MPU6050, *always on*)
* Optical encoders (2x, *always on*)
* IR side sensors (2x, *program switchable*)
* IR sensor (VS1838, *always on*)
* Light sensor (LDR, *always on*)
* Temperature sensor (LM35DZ, *always on*)
* Battery voltage
* Knock sensor SW420 (*always on*)
* Push buttons (3x)
* Potentiometers (2x)
* RGB LEDs (4xWS2812B, *always on*)
* LEDs (3x) + 2x White LEDs (headlights)
* LCD display (I2C 1602, *on by default*)
* Buzzer (Passive piezo)
* Bluetooth module (HC-02, *program switchable*)
* USB-UART module (CP2102, *powered by USB-C port*)

Communication
~~~~~~~~~~~~~

* **Bluetooth:** HC-02 (HC-05, HC-06 compatible)
* **WiFi:** ESP32-CAM (optional)
* **Serial:** Hardware UARTs (1 port + 1 port USB-UART)
* **I2C:** Multiple Devices
* **IR:** VS1838 (IR remote control)

Indicators
~~~~~~~~~~

* **Power LED:** 5V voltage provided
* **Power LED:** 3.3V voltage provided
* **Power LED:** 12V voltage enabled and provided
* **Charge LED:** charging in process
* **Charge LED:** Charging complete
* **Charge LED:** Charging level indicator (4 levels)
* **USB-UART LED:** USB-UART module data transfer activity
* **Bluetooth LED:** Bluetooth module status
* **IR LED:** IR side sensors activity status
* **Line following LED:** Line following activity status


Power Supply
~~~~~~~~~~~~

* **Battery type:** 1S Li-ion battery 18650
* **Voltage:** 3.7V - 4.2V
* **Capacity:** 2200+ mAh (recommended)
* **Charging current:** 1A
* **Current discharge rate (CDR):** 10A min 
* **Protection:** Battery protection system included (overcurrent 12A)
* **Runtime:** 1-3 hours
* **Charging time:** 2-4 hours
* **Charging:** Via USB-C port (TP4056 1A max) when device is powered off only

.. warning::
   During charging, the charging IC (e.g., TP4056) may become hot. This is normal at higher currents, but you must handle the device carefully and ensure proper ventilation. Do not touch the PCB components during charging and avoid charging near flammable materials.

Power supply provided
~~~~~~~~~~~~~~~~~~~~~

* **Output Voltage:** 5V (3A max)
* **Output Voltage:** 3.3V (3A max)
* **Output Voltage:** 12V (2A max) (program switchable)
* **Output power:** 45W max (5V + 3.3V + 12V)

Dimensions & Weight
~~~~~~~~~~~~~~~~~~~

* **Length:** ~142 mm
* **Width:** ~130 mm
* **Height:** ~60 mm
* **Weight:** ~370g (with battery)
* **Load capacity:** more than 2000g (tested with 750rpm motors)


