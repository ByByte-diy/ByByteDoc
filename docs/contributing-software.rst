Software & Libraries
====================

Contributing code, libraries, and tools to БАБАЙ project.

.. warning::
   **All software must be thoroughly tested before submission!**

Overview
--------

БАБАЙ software components:

* **Arduino Libraries** - Sensor/motor control libraries
* **Educational Tools** - Programming aids for students
* **Development Tools** - Tools for contributors
* **Example Projects** - Reference implementations
* **Testing Utilities** - Validation and testing tools

All code must be:

✅ **Well-documented** - Comments and guides
✅ **Tested** - Unit tests and examples
✅ **Educational** - Support learning
✅ **Compatible** - Work with both platforms
✅ **Open Source** - Proper licensing

Coding Standards
----------------

Arduino Code
~~~~~~~~~~~~

Follow Arduino style guide:

.. code-block:: cpp

   // Use meaningful names
   int ultrasonicSensorPin = 7;
   
   // Add comments explaining WHY, not just WHAT
   // Delay needed for sensor stabilization after power-on
   delay(1000);
   
   // Use constants for magic numbers
   const int THRESHOLD_DISTANCE = 20; // cm
   
   // Group related functionality
   void setupSensors() {
     pinMode(ultrasonicSensorPin, INPUT);
     // More sensor setup...
   }

**Naming Conventions:**

* Variables: ``camelCase``
* Constants: ``UPPER_SNAKE_CASE``
* Functions: ``camelCase``
* Classes: ``PascalCase``

Python Code
~~~~~~~~~~~

Follow PEP 8:

.. code-block:: python

   # Clear function names
   def calculate_distance(echo_time):
       """
       Calculate distance from ultrasonic sensor echo time.
       
       Args:
           echo_time: Time in microseconds
           
       Returns:
           Distance in centimeters
       """
       speed_of_sound = 343  # m/s at 20°C
       distance = (echo_time * speed_of_sound) / 2000000
       return distance

Other Languages
~~~~~~~~~~~~~~~

* Follow language-specific best practices
* Use linters and formatters
* Maintain consistency with existing code

Library Development
-------------------

Arduino Library Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   ByByteLibraryName/
   ├── src/
   │   ├── ByByteLibraryName.h      # Header file
   │   ├── ByByteLibraryName.cpp    # Implementation
   │   └── utility/                  # Helper files
   ├── examples/
   │   ├── BasicUsage/
   │   │   └── BasicUsage.ino
   │   └── AdvancedFeatures/
   │       └── AdvancedFeatures.ino
   ├── keywords.txt                  # Syntax highlighting
   ├── library.properties            # Library metadata
   ├── README.md                     # Documentation
   └── LICENSE                       # License file

Required Files
~~~~~~~~~~~~~~

**library.properties:**

.. code-block:: ini

   name=ByByte Robot Control
   version=1.0.0
   author=Your Name <email@example.com>
   maintainer=БАБАЙ Project
   sentence=Robot control library for БАБАЙ platforms
   paragraph=Provides easy control of motors, sensors, and peripherals
   category=Device Control
   url=https://github.com/vergilium/ByByte
   architectures=avr
   depends=Servo

**keywords.txt:**

.. code-block:: text

   ByByteRobot    KEYWORD1
   moveForward    KEYWORD2
   turnLeft       KEYWORD2

Documentation Requirements
---------------------------

Every Library Must Include
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **README.md**
   
   * What the library does
   * Installation instructions
   * Basic usage example
   * API reference
   * License information

2. **Examples**
   
   * At least 2-3 working examples
   * Comments explaining each step
   * Expected output
   * Hardware setup instructions

3. **API Documentation**
   
   * All public functions documented
   * Parameter descriptions
   * Return value descriptions
   * Usage examples

Example Documentation:

.. code-block:: cpp

   /**
    * Move robot forward at specified speed
    * 
    * @param speed Speed value from 0-255 (0=stop, 255=max)
    * @param duration Duration in milliseconds (0=continuous)
    * 
    * @return true if movement started successfully
    * 
    * Example:
    * @code
    * robot.moveForward(200, 1000);  // Move forward at speed 200 for 1 second
    * @endcode
    */
   bool moveForward(uint8_t speed, unsigned long duration = 0);

Testing Requirements
--------------------

All Code Must Be Tested
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Unit Tests**
   
   * Test individual functions
   * Check edge cases
   * Verify error handling

2. **Integration Tests**
   
   * Test with actual hardware
   * Test component interactions
   * Verify timing accuracy

3. **Example Tests**
   
   * All examples compile
   * Examples run correctly
   * Output matches documentation

Testing Tools
~~~~~~~~~~~~~

* **ArduinoUnit** - Unit testing for Arduino
* **PlatformIO** - Build and test automation
* **Hardware-in-the-loop** - Test with actual robots

Submission Process
------------------

1. **Proposal**
   
   Open GitHub Issue:
   
   .. code-block:: text

      Title: Library Proposal - [Library Name]
      
      Purpose: [What problem does it solve?]
      
      Features:
      - Feature 1
      - Feature 2
      
      Platform Support:
      - [X] БАБАЙ nano
      - [X] БАБАЙ Mega
      
      Dependencies: [List any required libraries]
      
      Educational Value: [How does it support learning?]

2. **Development**
   
   After approval:
   
   * Write clean, documented code
   * Create examples
   * Test thoroughly
   * Write documentation

3. **Code Review**
   
   Submit Pull Request:
   
   * Code follows standards
   * Tests pass
   * Documentation complete
   * Examples work

4. **Testing**
   
   Maintainers will:
   
   * Review code quality
   * Test with hardware
   * Verify educational value
   * Check compatibility

5. **Merge**
   
   Once approved:
   
   * Merge to main branch
   * Add to library index
   * Announce to community

Quality Checklist
-----------------

Before submitting:

- [ ] Code follows style guide
- [ ] All functions documented
- [ ] Examples included and tested
- [ ] README.md complete
- [ ] library.properties correct
- [ ] keywords.txt included
- [ ] Compatible with both platforms
- [ ] No warnings when compiling
- [ ] Tested with actual hardware
- [ ] Educational value clear
- [ ] License included

Common Pitfalls
---------------

Avoid These
~~~~~~~~~~~

❌ **No Documentation**
   * Always document your code

❌ **Hardcoded Values**
   * Use constants and parameters

❌ **No Error Handling**
   * Check for invalid inputs

❌ **Platform-Specific Code**
   * Ensure compatibility

❌ **Blocking Operations**
   * Use non-blocking approaches

❌ **Memory Leaks**
   * Properly manage resources

❌ **Uncommented Code**
   * Explain complex logic

Example Projects
----------------

Types of Contributions
~~~~~~~~~~~~~~~~~~~~~~

**Sensor Libraries:**

* Ultrasonic distance sensors
* Line following sensors
* IMU/gyroscope integration
* Environmental sensors

**Motor Control:**

* DC motor drivers
* Servo control
* Stepper motor control
* Speed regulation

**Navigation:**

* Obstacle avoidance
* Line following
* Path planning
* Localization

**Educational Tools:**

* Debugging utilities
* Calibration tools
* Serial monitors
* Configuration wizards

Code Templates
--------------

**Basic Arduino Library Template:**

.. code-block:: cpp

   // ByByteExample.h
   #ifndef BYBYTE_EXAMPLE_H
   #define BYBYTE_EXAMPLE_H
   
   #include <Arduino.h>
   
   class ByByteExample {
   public:
     ByByteExample(int pin);
     void begin();
     int readValue();
   
   private:
     int _pin;
   };
   
   #endif

**Implementation Template:**

.. code-block:: cpp

   // ByByteExample.cpp
   #include "ByByteExample.h"
   
   ByByteExample::ByByteExample(int pin) {
     _pin = pin;
   }
   
   void ByByteExample::begin() {
     pinMode(_pin, INPUT);
   }
   
   int ByByteExample::readValue() {
     return digitalRead(_pin);
   }

Resources
---------

* **Arduino Style Guide** - https://www.arduino.cc/en/Reference/StyleGuide
* **PEP 8** - https://pep8.org/
* **Git Workflow** - (see main contributing guide)
* **Testing Guide** - (to be added)

Questions?
----------

* Open GitHub Issue with tag ``software``
* Contact ``@vergilium``
* Join software development discussion

---

:doc:`Back to Contributing Overview <contributing>`
