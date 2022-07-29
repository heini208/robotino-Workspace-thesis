#!/usr/bin/env python3

from __future__ import print_function

from std_msgs.msg import Float32MultiArray
from robotino_msgs.srv import ResetOdometry

import rospy

def resetOdometryRobotino(data):
    if len(data.data) < 3:
        rospy.ServiceProxy('reset_odometry', ResetOdometry)(0, 0, 0)
    else:	
        rospy.ServiceProxy('reset_odometry', ResetOdometry)(data.data[0], data.data[1], data.data[2])


def resetOdometryTranslator():
    rospy.init_node('odometry_reset_node')
    rospy.Subscriber('reset_odometry', Float32MultiArray, resetOdometryRobotino)

    rospy.spin()

if __name__ == "__main__":
    resetOdometryTranslator()
