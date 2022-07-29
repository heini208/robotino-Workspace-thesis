# roberta-robotino-Workspace
catkin workspace to use the Robotino in the Open Roberta Lab



<h2> Installation: </h2>



**1. Connect the Robotino to your local Network**
For this you can use the tp-link-Travel Router or an Ethernet cable
To connect the Travel Router to the Internet you need to change it to client Mode for that you can connect the Travel Router to your pc and follow the Steps for Setting up the Client Mode found [here](https://ip.festo-didactic.com/InfoPortal/Robotino/document/wlan_quick.pdf)
It might be nessecary to set the instead of smart ip set the ip to a local ip in you network that is not already taken


**3 Connect to the robotino**
either ssh into the robotino using ssh robotino@robotino.local or instead of robotino.local you can use the ip of the robot (the default password is robotino)
or connect keyboard an mouse 

**2. Install ROS-Noetic Desktop onto the Robotino**

For the Installtion Process follow the ROS-Wiki Guide found [here](http://wiki.ros.org/noetic/Installation/Ubuntu)

**3. Copy the catkin_ws_roberta workspace from this repository somewhere onto the robotino**

**4. Run install.bash**
cd into the workspace
run: bash install.bash

**5. Done :)**



