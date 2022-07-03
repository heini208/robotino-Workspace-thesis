#!/usr/bin/env python3
import nav_msgs.msg
import rospy
import math, random
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

from robotino_msgs.srv import ResetOdometry  # für reset
from nav_msgs.msg import Odometry  # für get

try:
    rospy.init_node('robotino_go', anonymous=True)
    _motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)
except Exception as e:
    raise


def getOdom():
    odomX = rospy.wait_for_message("odom", Odometry).pose.pose.position.x
    odomY = rospy.wait_for_message("odom", Odometry).pose.pose.position.y

    yaw_z = 2 * math.acos(rospy.wait_for_message("odom", Odometry).pose.pose.orientation.w) * 180 / math.pi
    if rospy.wait_for_message("odom", Odometry).pose.pose.orientation.z < 0:
        yaw_z *= -1
    yaw_z

    return odomX, odomY, yaw_z


def run():
    print("starting roberta node...")
    rospy.sleep(0.3)

    # reset Odometry:
    # rospy.ServiceProxy('reset_odometry', ResetOdometry)(0, 0, 0)

    # get Odometry

    print("x:", getOdom()[0], " y:", getOdom()[1], " yaw_z:", getOdom()[2] )


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()
