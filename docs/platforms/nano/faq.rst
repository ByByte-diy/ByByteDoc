Frequently Asked Questions
==========================

Assembly Questions
~~~~~~~~~~~~~~~~~~

**Q: Do I need to solder anything?**

A: Yes, you need to solder the PCB but you need basic soldering skills and tools.

**Q: How long does assembly take?**

A: First-time builders: 1-2 hours. Experienced: 30-60 minutes.

**Q: Can I use different motors?**

A: Yes, as long as they're 6V - 12V DC motors same form factor as N20 motors. Adjust code for different speeds.

**Q: Where do I get the 3D printed parts?**

A: Options: Buy online, or 3D print from your 3D printer. The 3D printed parts not required for the assembly.

**Q: Can I add more sensors?**

A: Yes! If you not using the HC-0x bluetooth module you can add more sensors.

Component Questions
~~~~~~~~~~~~~~~~~~~

**Q: Arduino Nano or Uno?**

A: The PCB is designed for Arduino Nano compatible boards only.

**Q: What batteries should I use?**

A: 6F22 9v li-ion battery. You can use other 6V - 12V battery with replace the battery holder.

**Q: Can I use a power bank?**

A: For charging the battery you can use a power bank. Motors need separate battery.

**Q: My motor driver gets hot, is this normal?**

A: Slight warmth is OK. If very hot, check connections and reduce load.

Programming Questions
~~~~~~~~~~~~~~~~~~~~~

**Q: Which IDE should I use?**

A: Arduino IDE 2.0 (recommended) or Arduino IDE 1.8.x.

**Q: Where do I find example code?**

A: Arduino IDE > File > Examples > ByByte, or our GitHub repository.

**Q: My code won't upload, what's wrong?**

A: Check: Correct board selected, correct port, cable connected, drivers installed. Check the jumper settings on the PCB by ESP32-CAM module.

**Q: How do I debug my code?**

A: Use Serial.print() to output values, check connections, test components individually.