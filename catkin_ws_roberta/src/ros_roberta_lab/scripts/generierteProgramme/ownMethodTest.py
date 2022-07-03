#!/usr/bin/env python3

import rospy
import math, random
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

try:
    rospy.init_node('robotino_go', anonymous=True)
    _motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)
except Exception as e:
    raise


def startmotor(x, y, z):
    _twist = Twist()
    _twist.linear.x = 1 / 100 * x
    _twist.linear.y = 1 / 100 * y
    _twist.angular.z = 1 / 100 * z
    _motorPub.publish(_twist)


def run():
    print("starting roberta node...")
    rospy.sleep(0.3)

    startmotor(30, 30, 30)
    rospy.sleep(2000 / 1000)
    startmotor(0, 0, 0)
    rospy.sleep(2000 / 1000)



def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()
