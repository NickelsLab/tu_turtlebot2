cmake_minimum_required(VERSION 2.8.3)
project(tu_turtlebot_navigation)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
