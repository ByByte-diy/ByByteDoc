Technical Specifications
========================

Microcontroller
~~~~~~~~~~~~~~~~

* **Board:** Arduino Nano
* **Microcontroller:** ATmega328P
* **Operating Voltage:** 5V
* **Input Voltage:** 7-12V (recommended)
* **Digital I/O Pins:** 14
* **Analog Input Pins:** 6
* **Flash Memory:** 32 KB
* **SRAM:** 2 KB
* **EEPROM:** 1 KB
* **Clock Speed:** 16 MHz

Motors & Movement
~~~~~~~~~~~~~~~~~

* **Motor Type:** DC geared motors N20
* **Voltage:** 6V
* **RPM:** 400-750 (typical)
* **Motor Driver:** DRV8833
* **Speed Control:** PWM
* **Direction Control:** PWM

Sensors & peripherals
~~~~~~~~~~~~~~~~~~~~~

**Standard sensors:**

* Ultrasonic distance sensor (HC-SR04)
  
  * Range: 2-400 cm
  * Accuracy: ±3mm
  * Interface: Digital

* Line following sensors (IR-based)
  
  * Type: TCRT5000 or similar
  * Quantity: 5 sensors
  * Detection: Black/white surfaces
  * Interface: Digital

* IR side sensors (SFH4545, TEFT4300)
  
  * Type: SFH4545, TEFT4300 or similar
  * Quantity: 2 sensors
  * Range: 2-20 cm
  * Detection: IR emission
  * Interface: Analog
  
* IR receiver (VS1838)
  
  * Type: VS1838 or similar
  * Quantity: 1 sensor
  * Detection: IR pulse receiver
  * Interface: Digital
  
* Light sensor (LDR)
  
  * Type: LDR or similar
  * Quantity: 1 sensor
  * Detection: Light intensity
  * Interface: Analog

**Communication:**

* USB-UART port (for programming and debugging)
* Bluetooth module (HC-05, HC-06, HC-02)
* WiFi module (ESP32-CAM, optional)
* IR remote control (VS1838)

Power Supply
~~~~~~~~~~~~

* **Battery Type:** 6F22 9v li-ion battery
* **Voltage:** 7.4V - 9V
* **Capacity:** 1000+ mAh (recommended)
* **Runtime:** 1-2 hours (typical use)

Dimensions & Weight
~~~~~~~~~~~~~~~~~~~

* **Length:** ~140-200 mm
* **Width:** ~120-150 mm
* **Height:** ~80-100 mm
* **Weight:** ~150-200g (with batteries)