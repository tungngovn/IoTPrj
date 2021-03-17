#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32



def temp_callback(data):
    rospy.loginfo('Temperature %f', data.data)

def humid_callback(data):
	rospy.loginfo('Humidity %f', data.data)

##### Test fuction, fix later #####
def temp_actuator(data):
    if data.data > 25:
        rospy.loginfo('Hot!')
    else:
        rospy.loginfo('Cool')

##### Test fuction, fix later #####
def humid_actuator(data):
    if data.data > 80:
        rospy.loginfo('Too humid')
    else:
        rospy.loginfo('Kinda humid')

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/temperature', Float32, temp_callback)
    rospy.Subscriber('/humidity', Float32, humid_callback)
    rospy.Subscriber('/temperature', Float32, temp_actuator)
    rospy.Subscriber('/humidity', Float32, humid_actuator)

    rospy.spin()

if __name__ == '__main__':
    listener()
