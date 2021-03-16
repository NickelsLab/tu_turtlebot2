#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
    vel_msg = Twist()

    goal_angle = math.pi/2
    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 1 # rad/s

    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    
    while not rospy.is_shutdown():

        #Loop to move the turtle in an specified distance
        if(current_angle < goal_angle):
            print current_angle," < ",goal_angle
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_angle = vel_msg.angular.z*(t1-t0)
        else:
            #After the loop, stops the robot
            vel_msg.linear.x = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)
            break

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
