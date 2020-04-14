#!/usr/bin/env python
import roslib; roslib.load_manifest('athena_heart')
import rospy
import time
from instagram import Account, Media, WebAgent, Story, Location, Tag, Comment
import numpy
from std_msgs.msg import String
def instagram():
	pub = rospy.Publisher('chatter', String)
	rospy.init_node('instagram')
	while not rospy.is_shutdown():
		str = "hello world %s"%rospy.get_time()
		rospy.loginfo(str)
		pub.publish(String(str))
		rospy.sleep(3.0)
if __name__ == '__main__':
	try:
		instagram()
	except rospy.ROSInterruptException: pass
