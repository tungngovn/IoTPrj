#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

print('a')

temp_thres = 20
humid_thres = 50


def temp_callback(data):
    global alert
    print(data.data)

    if (data.data > temp_thres):
        alert.publish(1)
        rospy.sleep(1)
    rospy.loginfo('Temperature %f', data.data)

def humid_callback(data):
    global alert
    if (data.data > humid_thres):
        alert.publish(2)
    rospy.loginfo('Humidity %f', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    global alert 
    alert = rospy.Publisher('/alert', Float32, queue_size=2)

    rospy.Subscriber('/temperature', Float32, temp_callback)
    rospy.Subscriber('/humidity', Float32, humid_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()

