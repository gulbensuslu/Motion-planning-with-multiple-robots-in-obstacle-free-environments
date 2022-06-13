#! /usr/bin/env python

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/motion1.py


#nodeid = str(sys.argv[1])
#nodename = "turtle" + nodeid
import rospy
import sys
import math
import random 
from geometry_msgs.msg import Twist


nodeid = str(sys.argv[1])
nodename = "turtle" + nodeid
rospy.init_node(nodename,anonymous=True)
pub = rospy.Publisher(nodename +'/cmd_vel',Twist,queue_size=10)
vel_msg = Twist()

def moveLinear(distance): #this method used to linear motion  
	
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0

	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0 

	rate=rospy.Rate(10)

	t0=rospy.Time.now().to_sec() 
	current_distance = 0 
	
	while current_distance < distance :

		pub.publish(vel_msg) 
		t1=rospy.Time.now().to_sec() 
		current_distance = vel_msg.linear.x * (t1-t0)
		rate.sleep()

	#stop the robot, out of the loop
        vel_msg.linear.x = 0.0  
        vel_msg.angular.z = 0.0  
	pub.publish(vel_msg)

def decidemovingpath(DirectionOfMoving):  #In this function, it is decided how many degress the turtle's head will rotate.

	if DirectionOfMoving==0:  #left
		angle=90.0  
	else :		
		angle=270.0	 #right
 	return angle
	
def rotatehead(speed,angle,speedL,clockwise): #In this function,rotates the turtle in selected direction

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

def moveDown(): #This function makes the turtle move downwards

	down_distance = 0.2

	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0

	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0 

	rate=rospy.Rate(10)
	 
	t0=rospy.Time.now().to_sec() 
	current_distance = 0 
	
	while current_distance < down_distance :

		pub.publish(vel_msg) 
		t1=rospy.Time.now().to_sec() 
		current_distance = vel_msg.linear.x * (t1-t0)
		rate.sleep()

	#stop the robot, out of the loop
        vel_msg.linear.x = 0.0  
        vel_msg.angular.z = 0.0  
	pub.publish(vel_msg)

if __name__ == "__main__": 
	
	try:
		firstDistance = 0.5
		secondDistance=0 
		thirdDistance=0

		firstDirectionOfMoving=1 #right
		secondDirectionOfMoving=1 #right
		thirdDirectionOfMoving=0 #left
		leftMoving=0
		
		
		if(firstDirectionOfMoving == secondDirectionOfMoving):
			secondDistance=firstDistance+0.1
		else :
			secondDistance=firstDistance*2

		if(secondDirectionOfMoving == thirdDirectionOfMoving):
			thirdDistance=secondDistance+0.1
		else :
			thirdDistance=secondDistance*2
			
		#round1
		moveLinear(firstDistance)
		rotatehead(20,decidemovingpath(firstDirectionOfMoving),0,1)
		moveDown()
		rotatehead(20,decidemovingpath(firstDirectionOfMoving),0,1)
		moveLinear(firstDistance)

 		rotatehead(20,decidemovingpath(leftMoving),0,1)
		moveDown()
		rotatehead(20,decidemovingpath(leftMoving),0,1)

		#round2
		moveLinear(secondDistance)
		rotatehead(20,decidemovingpath(secondDirectionOfMoving),0,1)
		moveDown()
		rotatehead(20,decidemovingpath(secondDirectionOfMoving),0,1)
		moveLinear(secondDistance)

		#round3
		moveLinear(thirdDistance)
		rotatehead(20,decidemovingpath(thirdDirectionOfMoving),0,1)
		moveDown()
		rotatehead(20,decidemovingpath(thirdDirectionOfMoving),0,1)
		moveLinear(thirdDistance)


	except rospy.ROSInterruptException:
		pass 

		




























