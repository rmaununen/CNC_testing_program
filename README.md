# CNC testing program
This is a testing program for a CNC machine based on Arduino and 4 stepper motors. With this program you can manually control the rotation (both speed and direction) of stepper motors in real time. Pygame module is used to create the testing interface. Serial module is used for communication with the controller. Designed for the following configuration: Arduino Nano, four Nema 17 (17HS4401) stepper motors, four A4988 drivers. However, it can also be used with different models of Arduino or stepper motors (check out the installation instructions). 

# Installation
0) Check if you have python modules installed: serial, pygame, numpy
1) In controller.ino change the digital pins to the ones that you are using
2) If you are using different stepper motors, check their number of steps per revolution (from the datasheet). Change this number in controller.ino. Also check the speed limits of your motors (look it up somewhere or determine experimentally) and change the corresponding variables in both controller.ino and main.py
3) Download the firmware (controller.ino) to your Arduino
4) In main.py change the port name to the one that you are using
5) Run main.py
