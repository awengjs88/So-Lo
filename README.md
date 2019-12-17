# So-Lo
Senior Design Project
So-Lo (Sound Locator) is a real-time automated video and audio recording system that can locate the direction that a person is speaking in a small to medium-sized room for the purpose of recording meetings. The device is a simple camera mounted on top of a motor. To locate the direction of the speaker, the device uses time delay of arrival. Essentially, three microphones are set up in a triangular array, one foot apart from each other, with the camera and motor in the epicenter. The device determines which angle the speaker is, relative to the camera, based on which microphone picks up the voice first, second, and third using a series of complex mathematical equations. 

# Requirements
The system uses a Raspberry Pi 3, Arduino, and other various hardware components to operate. The system is broken up into four subsystems: the microphones, time interrupt system, angle calculation, and motor subsystem. 

The three microphones are simple electret omnidirectional microphones whose purpose is to pick up sound generated from a person speaking. Since the signal going into the microphones was very weak, an amplifier (TL074CN) was used to strengthen the signal. This is also important because people may be talking from varying distances away from the microphones in the room. 

The time interrupt system's job was to time stamp the time in which each microphone receives a signal. This system was implemented in an Arduino (Teensy 3.5) instead of the main Raspberry Pi 3. The reason for this was because the Arduino does not run an operating system which means it could dedicate more CPU cycles to its task and get a more accurate reading. This system was written in C++ and operated within the Arduino.

The angle calculation system takes the time stamps from the time interrupt system to calculate to time delays between the microphones. Using the time delays, the system determines the angle that the signal was located at relative to the camera. The formula is basically a system of three circle equations. The angle calculation was purely software implemented in Python and operated within the Raspberry Pi 3. 

The motor subsystem takes the angle calculated by the angle calculation subsystem and turns the camera to the specified angle. The motor of choice was a Maxon DC brush motor. A motor driver chip (L293D) was also used to control the motor for two reasons: in order to spin the motor clockwise and counter-clockwise and because the Raspberry Pi 3 GPIO pins are not capable of supplying enough power to the motor. An E5 optical encoder was used in order for the system to identify the direction it is facing. Since the motor can be moved while the device is unpowered, a home position was implemented using a photointerrupter (H21A1). When the device is powered on, it will automatically turn until the camera is facing the home position. The motor control software was written in Python and operates within the Raspberry Pi 3. The home position software was written in C++ and operates within the Arduino.

# Running homepos.ino
1. Download the [Arduino IDE](https://www.arduino.cc/en/main/software)
2. Run homepos.ino
3. If there is a prompt to create a directory for homepos.ino, hit confirm.

# Running motor.py
1. On a Raspberry Pi 3, open the terminal
2. Change the directory to where motor.py is stored
3. Type in motor.py
