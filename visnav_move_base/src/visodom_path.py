#!/usr/bin/python
import rospy
from geometry_msgs.msg import Twist
from move_base_path2 import *


if __name__ == '__main__':
    try:
        # Starts a new node
        rospy.init_node('visodom_path_follower', anonymous=True)
        velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)

        #cap = cv2.VideoCapture(0) # use /dev/video0
        cap = cv2.VideoCapture(1) # use /dev/video1
#	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,533)
#	cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1200)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH,1600)


        # start at 3,0
        move_fwd(velocity_publisher,cap,0.5)
        move_rot(velocity_publisher,cap, math.pi/4)
        move_fwd(velocity_publisher,cap,0.707)
        move_rot(velocity_publisher,cap, math.pi/4)
        move_fwd(velocity_publisher,cap,1.0)
        move_rot(velocity_publisher,cap,-math.pi/2)
        move_fwd(velocity_publisher,cap,1.0)

    except rospy.ROSInterruptException: pass
