Quick Start Guide
=================

This quick start guide will help you get up and running with ByByte in minutes.

Basic Usage
-----------

Upload the firmware to your Arduino:

.. code-block:: bash

   # Compile and upload
   arduino-cli compile --fqbn arduino:avr:uno
   arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno

First Example
-------------

Here's a simple example to get you started:

.. code-block:: python

   import bybyte

   # Initialize connection
   device = bybyte.connect('/dev/ttyACM0')
   
   # Send command
   response = device.send_command('status')
   print(f"Device status: {response}")

   # Close connection
   device.close()

Common Commands
---------------

* ``status`` - Get device status
* ``reset`` - Reset the device
* ``info`` - Get device information

Configuration
-------------

Basic configuration options:

.. code-block:: ini

   [device]
   port = /dev/ttyACM0
   baudrate = 9600
   timeout = 5

   [logging]
   level = INFO
   file = bybyte.log

Next Steps
----------

* Read the full :doc:`usage` guide
* Check the :doc:`api` reference
* Explore example projects

Troubleshooting
---------------

**Connection Issues**

If you can't connect to the device:

1. Check that the device is properly connected
2. Verify the correct port is specified
3. Ensure no other program is using the port

**Permission Denied**

On Linux, you may need to add your user to the ``dialout`` group:

.. code-block:: bash

   sudo usermod -a -G dialout $USER
   # Log out and log back in for changes to take effect

