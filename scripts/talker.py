#!/usr/bin/env python

import Adafruit_DHT
import RPi.GPIO as GPIO
import time

import rospy
from std_msgs.msg import String, Float32

Adafruit_DHT ho tro nhieu loai cam bien DHT, o day dung DHT11 nen chon cam bien  DHT11
chon_cam_bien = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)

# chan DATA duoc noi vao chan GPIO25 cua PI
pin_sensor = 25

def talker():
    # pub = rospy.Publisher('chatter', String, queue_size=10)
    temperature = rospy.Publisher('temperature', Float32, queue_size=10)
    humidity = rospy.Publisher('humidity', Float32, queue_size=10)
    rospy.init_node('temperature_humidity', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        do_am, nhiet_do = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor);

        temperature.publish(nhiet_do)
        humidity.publish(do_am)

        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(do_am)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
