#!/usr/bin/env python3

import rospy
import math, random
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from nav_msgs.msg import Odometry  # für get
from robotino_msgs.srv import ResetOdometry  # für reset


try:
    rospy.init_node('robotino_go', anonymous=True)
    _motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)
except Exception as e:
    raise


# TODO method generated
def driveForDistance(xSpeed, ySpeed, distance):
    print(rospy.wait_for_message("odom", Odometry).pose.pose.position.x)
    xStart = rospy.wait_for_message("odom", Odometry).pose.pose.position.x
    yStart = rospy.wait_for_message("odom", Odometry).pose.pose.position.y
    if distance < 0:
        startmotor(-xSpeed, -ySpeed, 0)
    else:
        startmotor(xSpeed, ySpeed, 0)
    distance = abs(distance)
    while True:
        xPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.x
        yPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.y
        currentDistance = math.sqrt(math.pow(xPos - xStart, 2) + math.pow(yPos - yStart, 2))
        if currentDistance * 100 >= distance:
            startmotor(0, 0, 0)
            break
        rospy.Rate(10).sleep()
    print(rospy.wait_for_message("odom", Odometry).pose.pose.position.x)



def startmotor(x, y, z):
    _twist = Twist()
    _twist.linear.x = 1 / 100 * x * 0.2
    _twist.linear.y = 1 / 100 * y * 0.2
    _twist.angular.z = 1 / 100 * z
    _motorPub.publish(_twist)


def run():
    print("starting roberta node...")
    rospy.ServiceProxy('reset_odometry', ResetOdometry)(0, 0, 0)
    rospy.sleep(0.3)

    driveForDistance(100, 0, -40)


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()
