#!/usr/bin/env python3
import rospy
import math, random
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from robotino_msgs.srv import ResetOdometry

rospy.init_node('robotino_go', anonymous=True)
_motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)
_safetyPub = rospy.Publisher('safety_mode', Bool, queue_size=10)


def _getOrientation():
    yaw_z = 2 * math.acos(rospy.wait_for_message("odom", Odometry).pose.pose.orientation.w)
    if rospy.wait_for_message("odom", Odometry).pose.pose.orientation.z < 0:
        yaw_z *= -1
    return yaw_z


def _setSpeedOmnidrive(x, y, z):
    twist = Twist()
    twist.linear.x = (1 / 100 * x) * 0.2
    twist.linear.y = (1 / 100 * y) * 0.2
    twist.angular.z = 1 / 100 * z
    _motorPub.publish(twist)


def _turnForDegrees(speed, degrees):
    start = _getOrientation() * (180 / math.pi) % 360
    target = (start + degrees) % 360
    fullRotations = abs(degrees / 360)
    _setSpeedOmnidrive(0, 0, speed)
    lastDistance = 370
    orientation = start
    print("target: ", target)
    while True:

        distance = abs(target - orientation)
        if (target > orientation and speed >= 0) or (target > orientation and speed <= 0):
            distance = 360 - distance
        print("distance: ", distance, "lastDistance:", lastDistance, "fullRotations:", fullRotations)

        if distance > lastDistance or distance <= 0:
            if fullRotations < 1:
                _setSpeedOmnidrive(0, 0, 0)
                print(orientation, "fullRotations:", fullRotations)
                break
            else:
                distance = 360
                fullRotations -= 1
        lastDistance = distance
        orientation = _getOrientation() * (180 / math.pi) % 360
        # orientation am ende wegen 360 grad sodass 360 drehung nicht 720 grad wird


def run():
    print("starting roberta node...")
    rospy.ServiceProxy('reset_odometry', ResetOdometry)(0, 0, 0)
    rospy.sleep(0.3)
    _safetyBoolean = Bool()
    _safetyBoolean.data = True
    _safetyPub.publish(_safetyBoolean)

    _turnForDegrees(-50, -180)
    rospy.sleep(3)
    _turnForDegrees(100, 180)


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()
