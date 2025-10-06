API Reference
=============

This page contains the complete API reference for ByByte.

Core Classes
------------

Device
~~~~~~

.. code-block:: python

   class Device:
       """Main device class for communicating with Arduino."""

       def __init__(self, port, baudrate=9600, timeout=5):
           """
           Initialize device connection.

           :param port: Serial port path (e.g., '/dev/ttyACM0')
           :param baudrate: Communication speed (default: 9600)
           :param timeout: Connection timeout in seconds
           """
           pass

       def connect(self):
           """Establish connection to device."""
           pass

       def disconnect(self):
           """Close connection to device."""
           pass

       def send_command(self, command, **kwargs):
           """
           Send command to device.

           :param command: Command string
           :param kwargs: Additional command parameters
           :return: Device response
           """
           pass

       def is_connected(self):
           """
           Check if device is connected.

           :return: True if connected, False otherwise
           """
           pass

Connection Functions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def connect(port, baudrate=9600, timeout=5):
       """
       Create and connect to a device.

       :param port: Serial port path
       :param baudrate: Communication speed
       :param timeout: Connection timeout
       :return: Connected Device instance
       """
       pass

   def scan_devices():
       """
       Scan for available devices.

       :return: List of available port names
       """
       pass

Exceptions
----------

ConnectionError
~~~~~~~~~~~~~~~

Raised when connection to device fails.

.. code-block:: python

   class ConnectionError(Exception):
       """Failed to connect to device."""
       pass

TimeoutError
~~~~~~~~~~~~

Raised when operation exceeds timeout.

.. code-block:: python

   class TimeoutError(Exception):
       """Operation timed out."""
       pass

CommandError
~~~~~~~~~~~~

Raised when command execution fails.

.. code-block:: python

   class CommandError(Exception):
       """Command execution failed."""
       pass

Utilities
---------

Logging
~~~~~~~

.. code-block:: python

   def setup_logging(level='INFO', filename=None):
       """
       Configure logging for ByByte.

       :param level: Logging level (DEBUG, INFO, WARNING, ERROR)
       :param filename: Optional log file path
       """
       pass

Configuration
~~~~~~~~~~~~~

.. code-block:: python

   class Config:
       """Configuration manager."""

       @staticmethod
       def load(filename):
           """
           Load configuration from file.

           :param filename: Path to config file
           :return: Configuration dictionary
           """
           pass

       @staticmethod
       def save(config, filename):
           """
           Save configuration to file.

           :param config: Configuration dictionary
           :param filename: Path to config file
           """
           pass

Examples
--------

Basic Connection
~~~~~~~~~~~~~~~~

.. code-block:: python

   import bybyte

   # Connect to device
   device = bybyte.connect('/dev/ttyACM0', baudrate=9600)

   # Send command
   response = device.send_command('status')
   print(response)

   # Close connection
   device.close()

With Context Manager
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   with bybyte.connect('/dev/ttyACM0') as device:
       response = device.send_command('get_temperature')
       print(f"Temperature: {response}°C")

Scanning for Devices
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Find available devices
   ports = bybyte.scan_devices()
   print(f"Available ports: {ports}")

   # Connect to first available
   if ports:
       device = bybyte.connect(ports[0])
       print(f"Connected to {ports[0]}")

