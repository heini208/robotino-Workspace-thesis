#!/usr/bin/env python3

import rospy
import math, random
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

rospy.init_node('robotino_go', anonymous=True)

_motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)
_twist = Twist()


def run():
    global _twist, _motorPub
    print("starting roberta node...")
    rospy.sleep(0.3)

    _twist.linear.x = 1 / 100 * 0
    _twist.linear.y = 1 / 100 * -30
    _twist.angular.z = 1 / 100 * 0
    _motorPub.publish(_twist)

    rospy.sleep(2000 / 1000)


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()
