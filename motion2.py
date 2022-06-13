#!/usr/bin/env python

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/motion2.py

import rospy
import sys
import math
from geometry_msgs.msg import Twist


#rospy.init_node('move')
#pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

nodeid = str(sys.argv[1])
nodename = "turtle" + nodeid
rospy.init_node(nodename,anonymous=True)
pub = rospy.Publisher(nodename +'/cmd_vel',Twist,queue_size=10)

vel_msg = Twist()

vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0

vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0 

def drawhalfcircles(speed,angle,speedL,clockwise): #in this method, turtle draws half circles like spiral
	speedAngular= speed * (math.pi/180.0)
	relativeAngle= angle * (math.pi/180.0)
	vel_msg.linear.x = speedL
	vel_msg.angular.z = speedAngular * clockwise

	rate=rospy.Rate(10)
	
	t0=rospy.Time.now().to_sec() 
	angleCurrent= 0 
	
	while   angleCurrent < relativeAngle:

		pub.publish(vel_msg) 
		t1=rospy.Time.now().to_sec()
		angleCurrent = speedAngular * (t1-t0)
		rate.sleep()

	#stop the robot, out of the loop
        vel_msg.linear.x = 0.0  
        vel_msg.angular.z = 0.0  
	pub.publish(vel_msg)


if __name__ == "__main__": 
	try:
		radius= 0.3
		for i in range (5):
			drawhalfcircles(50, 180,radius, -1)
			radius=radius + 0.2
			i=i+1

	except rospy.ROSInterruptException:
		pass 
