#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
import numpy as np
import cv2
import time

# v2 - take a picture every so often

# move the base along a prescribed path
# (vel v1 for time t1, v2 for time t2, etc...) - dead reconing

lin_speed = 0.10 # m/s
ang_speed = 1.0 # rad/s

vel_msg = Twist()

def move_rot (velocity_publisher,cap,angle):
    print "Rotating by %.2f deg (%.2f rad)" % (math.degrees(angle),angle)
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    vel_msg.angular.z = np.sign(angle) * ang_speed

    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle    = 0
    
    while not rospy.is_shutdown():
        _, frame = cap.read()
        filename = time.strftime("/tmp/ceil-%Y%m%d-%H%M%S.jpg")
        cv2.imwrite(filename,frame)

        #Loop to move the turtle in an specified distance
        if(current_angle    < abs(angle)):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()          # Takes actual time to velocity calculus
            current_angle = ang_speed*(t1-t0)       # Calculates distancePoseStamped
        else:
            #After the loop, stops the robot
            vel_msg.linear.x = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)
            break



def move_fwd (velocity_publisher,cap,distance):
    print "Moving fwd by %.2f meters" % (distance)
    vel_msg.linear.x = np.sign(distance) * lin_speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    
    while not rospy.is_shutdown():
        _, frame = cap.read()
        filename = time.strftime("/tmp/ceil-%Y%m%d-%H%M%S.jpg")
        cv2.imwrite(filename,frame)

        #Loop to move the turtle in an specified distance
        if(current_distance < abs(distance)):
            # print current_distance," < ",distance
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()          # Takes actual time to velocity calculus
            current_distance= lin_speed*(t1-t0)       # Calculates distancePoseStamped
        else:
            #After the loop, stops the robot
            vel_msg.linear.x = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)
            break




if __name__ == '__main__':
    try:
        # Starts a new node
        rospy.init_node('robot_cleaner', anonymous=True)
        velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)

        move_fwd(velocity_publisher,0.2)
        move_fwd(velocity_publisher,-0.2)

        move_rot(velocity_publisher,math.pi/2.0)
        move_rot(velocity_publisher,-math.pi/2.0)

    except rospy.ROSInterruptException: pass
