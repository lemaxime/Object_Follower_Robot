# Object_Follower_Robot
### Description
Raspberry Pi 4, Open-CV based robot aiming at detecting a given object and following it.

### About the OpenCV Library
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.

### About the Raspberry Pi
The Raspberry Pi is a low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python. It’s capable of doing everything you’d expect a desktop computer to do, from browsing the internet and playing high-definition video, to making spreadsheets, word-processing, and playing games.

## Introduction
Me and my team mate created a Raspberry Pi 4 based robot using the OpenCV image recognition library.
We aimed at controlling the 4-wheeled chassis with the camera feedback.
The camera is checking for every object in its field of vision. If the object is in the preset list of the aimed object, a box appear around the object in the camera feedback.
If the box is not centered the robot is orienting itself to center the object. Once the box is centered the robot goes forward.

In our proof of concept, the robot must chase a cup of coffee.

### Project's Hardware
- a 4 wheeled-chassis, 
- 4 motors, 
- a h-bridge circuit, 
- a Raspberry Pi 4, 
- an USB camera 
- a pack of batteries.

### Project's Software
- Raspberry Pi OS (last version to date on the 17th October)
- Python3
- OpenCV
- VS Code

### Procedure
#### Robot connections
![Circuit diagram](https://github.com/lemaxime/Object_Follower_Robot/blob/2a72fdba54e8b2cac394b938bfafca66162d9d33/Circuit_diagram.HEIC)

#### Installing Raspberry Pi 4
We choose to install Raspberry using SSH (Secure Shell) to avoid spending ressources with the UX. It's an easy procedure as long as you follow those steps :
- Install the Raspberry Pi Imager on your PC
- Put the SD Card in the reader then choose the last full version of the OS, the SD Card and press `Command + Shift + X` to open the option pannel in which you need to check the following boxes : choose hostname, activate SSH and put a password, configure WIFI (a Wifi networks that doens't prevent IoT to connect).
- Find the IP address with `arp -a`
- Connect to the Raspberry with `ssh pi@'IP address of the Raspberry'`

> The USB camera we used worked out of the box. We tried to use the camera that was in the Raspberry Pi 4 kit but never managed to set it up. To test the camera, you could try to run the code using the UX by connecting the Raspberry to the a screen or by using VNC (after having enabled it with `sudo raspi-config` under INTERFACE / VNC.

#### Setup the code
Create a folder and put all the files in it.
Install OpenCV in the terminal with `pip install opencv-python`
Note that you can modify the code using `nano + name` and lunch it using `python3 + name`
