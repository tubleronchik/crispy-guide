#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import time
from instagram import Account, Media, WebAgent, Story, Location, Tag, Comment
agent = WebAgent()
account = Account("mixit_ru")

posts = agent.get_media(account, pointer=None, count=5)


def data():
    res = list(list(posts)[0])
    i = 0 #counts of posts
    likes = []
    likes_prev = []
    comments = []
    comments_prev = []
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('insta', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        media = Media(res[i])
        likes.append(media.likes_count)
        comments.append(media.comments_count)
        i += 1
        if i == len(res):
                likes_prev = likes
                likes = []
                comments_prev = comments
                comments = []
                time.sleep(3)	

                for i in range(len(res)):
                        media = Media(res[i])
                        agent.update(media)
                        likes.append(media.likes_count)
                        comments.append(media.comments_count)

                        if likes_prev[i] < likes[i] or comments_prev[i] < comments[i]:
                                        beats = "Beats!"
                                        rospy.loginfo(beats)
                                        pub.publish(beats)
                                        rate.sleep()


                likes = []
                likes_prev = []
                comments = []
                comments_prev = []
                i = 0

if __name__ == '__main__':
    try:
        data()
    except rospy.ROSInterruptException:
       pass

