# tu_turtlebot
Code developed for local turtlebot2
This has:
* developed under ros-kinetic
* has hokoyu lidar URDF and scanners integrated
* some basic move base commands
* worked with Trinity's turtlebot2 base

# branch melodic-devel
## setup for operation under ros-melodic
0) sudo apt install python3-vcstool
1) sudo apt-get install ros-melodic-catkin python-catkin-tools 
2) mkdir -p ~/code/tu_turtlebot_ws
3) cd ~/code/tu_turtlebot_ws
4) git clone git@github.com:NickelsLab/tu_turtlebot2.git
4a) cd tu_turtlebot2
4b) git checkout melodic-devel
4c) mkdir ../src; cd ../src
5) vcs import < ../tu_turtlebot2/repos
6) source /opt/ros/melodic/setup.bash
7) cd ..; rosdep install --from-paths src --ignore-src -r -y
8) catkin build
9) source devel/setup.bash
10) rosrun robot_upstart install tu_turtlebot_bringup/launch/lidar.launch 

## teleop (from another machine, say ros2)
1) export ROS_IP=131.194.84.216 (ip of ros2)
2) export ROS_MASTER_URI=http://131.194.115.203:11311 (ip of nano)
3) source ~/tu_turtlebot_ws/devel/setup.bash
3) rviz -d `rospack find tu_turtlebot_bringup`/../../basic_config.rviz &
4) roslaunch turtlebot_teleop logitech.launch
4a) hold down LB and use left joystick to drive around!

