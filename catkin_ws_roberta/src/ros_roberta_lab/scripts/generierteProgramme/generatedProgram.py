#!/usr/bin/env python3
import rospy
import math, random
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from robotino_msgs.srv import ResetOdometry

rospy.init_node('robotino_go', anonymous=True)
_motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)


def _getOrientation():
    yaw_z = 2 * math.acos(rospy.wait_for_message("odom", Odometry).pose.pose.orientation.w) * 180 / math.pi
    if rospy.wait_for_message("odom", Odometry).pose.pose.orientation.z < 0:
        yaw_z *= -1
    return yaw_z


def _setSpeedOmnidrive(x, y, z):
    _twist = Twist()
    _twist.linear.x = (1 / 100 * x) * 0.2
    _twist.linear.y = (1 / 100 * y) * 0.2
    _twist.angular.z = 1 / 100 * z
    _motorPub.publish(_twist)


def macheEtwas():
    print(rospy.wait_for_message("odom", Odometry).pose.pose.position.x)
    print(rospy.wait_for_message("odom", Odometry).pose.pose.position.y)
    print(_getOrientation())


def run():
    print("starting roberta node...")
    rospy.ServiceProxy('reset_odometry', ResetOdometry)(0, 0, 0)
    rospy.sleep(0.3)

    print("1:")
    macheEtwas()
    _setSpeedOmnidrive(30, 0, 0)
    rospy.sleep(1000 / 1000)
    print("2:")
    macheEtwas()
    _setSpeedOmnidrive(0, 0, -30)
    rospy.sleep(1000 / 1000)
    _motorPub.publish(Twist())

    rospy.sleep(500 / 1000)
    print("3:")
    macheEtwas()
    rospy.ServiceProxy('reset_odometry', ResetOdometry)(rospy.wait_for_message("odom", Odometry).pose.pose.position.x,
                                                        rospy.wait_for_message("odom", Odometry).pose.pose.position.y,
                                                        0)
    rospy.sleep(1000 / 1000)
    print("afterReset")
    macheEtwas()


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()