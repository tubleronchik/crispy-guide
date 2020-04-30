#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import String
def callback(data):
    rospy.loginfo(rospy.get_name()+"I heard %s",data.data)
    pwm.start(9)
    rospy.sleep(1.0)
    pwm.ChangeDutyCycle(7)
def listener():
     rospy.init_node('servo', anonymous=True)
     rospy.Subscriber("chatter", String, callback)
     rospy.spin()
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 50)

if __name__ == '__main__':
    listener()
