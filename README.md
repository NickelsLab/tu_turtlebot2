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
1) mkdir -p ~/code/tu_turtlebot_ws
2) cd ~/code/tu_turtlebot_ws
3) git clone git@github.com:NickelsLab/tu_turtlebot2.git
3a) cd tu_turtlebot2
3b) git checkout melodic-devel
3c) cd ../src
4) vcs import < tu_turtlebot2/repos
5) source /opt/ros/melodic/setup.bash
6) rosdep install --from-paths src --ignore-src -r -y
7) catkin build
8) source devel/setup.bash
9) rosrun robot_upstart install tu_turtlebot_bringup/launch/lidar.launch 

## teleop (from another machine, say ros2)
1) export ROS_IP=131.194.84.216 (ip of ros2)
2) export ROS_MASTER_URI=http://131.194.115.203:11311 (ip of nano)
3) source ~/tu_turtlebot_ws/devel/setup.bash
3) rviz -d `rospack find tu_turtlebot_bringup`/../../basic_config.rviz &
4) roslaunch turtlebot_teleop logitech.launch
4a) hold down LB and use left joystick to drive around!

