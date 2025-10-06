Usage Guide
===========

This guide covers the main features and usage patterns of ByByte.

Overview
--------

ByByte provides a simple interface for communicating with Arduino-based devices.

Basic Concepts
--------------

Connection Management
~~~~~~~~~~~~~~~~~~~~~

Managing device connections:

.. code-block:: python

   import bybyte

   # Open connection
   device = bybyte.connect(port='/dev/ttyACM0', baudrate=9600)

   try:
       # Use the device
       result = device.send_command('status')
       print(result)
   finally:
       # Always close the connection
       device.close()

Using context manager (recommended):

.. code-block:: python

   with bybyte.connect('/dev/ttyACM0') as device:
       result = device.send_command('status')
       print(result)

Sending Commands
~~~~~~~~~~~~~~~~

Send commands to your device:

.. code-block:: python

   # Simple command
   response = device.send_command('get_temperature')

   # Command with parameters
   response = device.send_command('set_led', color='red', brightness=128)

   # Wait for response with timeout
   response = device.send_command('long_operation', timeout=30)

Advanced Features
-----------------

Async Operations
~~~~~~~~~~~~~~~~

For non-blocking operations:

.. code-block:: python

   import asyncio
   from bybyte import AsyncDevice

   async def main():
       async with AsyncDevice.connect('/dev/ttyACM0') as device:
           result = await device.send_command_async('status')
           print(result)

   asyncio.run(main())

Event Handling
~~~~~~~~~~~~~~

Listen for device events:

.. code-block:: python

   def on_data_received(data):
       print(f"Received: {data}")

   device.on('data', on_data_received)
   device.start_listening()

Configuration
-------------

You can configure ByByte using a configuration file or environment variables.

Configuration File
~~~~~~~~~~~~~~~~~~

Create a ``config.ini`` file:

.. code-block:: ini

   [device]
   port = /dev/ttyACM0
   baudrate = 9600
   timeout = 5

   [advanced]
   buffer_size = 1024
   retry_attempts = 3

Load configuration:

.. code-block:: python

   device = bybyte.connect_from_config('config.ini')

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

Alternatively, use environment variables:

.. code-block:: bash

   export BYBYTE_PORT=/dev/ttyACM0
   export BYBYTE_BAUDRATE=9600

Best Practices
--------------

1. **Always close connections** - Use context managers when possible
2. **Handle exceptions** - Wrap operations in try-except blocks
3. **Set appropriate timeouts** - Prevent hanging operations
4. **Validate responses** - Check command responses before using them
5. **Log operations** - Enable logging for debugging

Error Handling
--------------

Common exceptions and how to handle them:

.. code-block:: python

   from bybyte.exceptions import (
       ConnectionError,
       TimeoutError,
       CommandError
   )

   try:
       device = bybyte.connect('/dev/ttyACM0')
       response = device.send_command('status')
   except ConnectionError as e:
       print(f"Failed to connect: {e}")
   except TimeoutError as e:
       print(f"Operation timed out: {e}")
   except CommandError as e:
       print(f"Command failed: {e}")
   finally:
       if device:
           device.close()

See Also
--------

* :doc:`api` - Complete API reference
* :doc:`quickstart` - Quick start guide
* :doc:`contributing` - Contributing guidelines

