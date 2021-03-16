#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32



def temp_callback(data):
    rospy.loginfo('Temperature %f', data.data)

def humid_callback(data):
	rospy.loginfo('Humidity %f', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/temperature', Float32, temp_callback)
    rospy.Subscriber('/humidity', Float32, humid_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
