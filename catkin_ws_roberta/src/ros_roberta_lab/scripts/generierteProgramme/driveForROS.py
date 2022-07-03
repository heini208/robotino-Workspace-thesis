#!/usr/bin/env python3

import rospy
import math, random
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from nav_msgs.msg import Odometry  # für get

try:
    rospy.init_node('robotino_go', anonymous=True)
    _motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)
except Exception as e:
    raise


# TODO method generated
def driveForDistance(xSpeed, ySpeed, distance):
    xStart = rospy.wait_for_message("odom", Odometry).pose.pose.position.x
    yStart = rospy.wait_for_message("odom", Odometry).pose.pose.position.y
    startmotor(xSpeed, ySpeed, 0)
    targetX, targetY = getTargetCoordinates(xSpeed, ySpeed, xStart, yStart, distance)
    while True:
        xPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.x
        yPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.y
        print("xPos: ", xPos, "yPos: ", yPos, "\nxTarget: ", targetX, "yTarget: ", targetY, "\nxSpeed: ", xSpeed,
              " ySpeed: ", ySpeed, "\n")
        if xSpeed > 0 and (xPos >= targetX) or xSpeed == 0:
            if yPos > 0 and (yPos >= targetY) or ySpeed == 0:
                break
            elif yPos < 0 and (yPos <= targetY):
                break
        elif xSpeed < 0 and xPos <= targetX:
            if yPos >= 0:
                if yPos > 0 and (yPos >= targetY) or ySpeed == 0:
                    break
                elif yPos < 0 and (yPos <= targetY):
                    break
        rospy.Rate(10).sleep()
    startmotor(0, 0, 0)


# TODO method generated + braucht odometrie und motor als hardware
def getTargetCoordinates(xSpeed, ySpeed, xStart, yStart, distance):
    maxSpeed = 1
    speedXMs = xSpeed / 100 * maxSpeed
    speedYMs = ySpeed / 100 * maxSpeed
    absV = math.sqrt(math.pow(speedXMs, 2) + math.pow(speedYMs, 2))
    x0 = speedXMs / absV
    y0 = speedYMs / absV
    xL = distance / 100 * x0
    yL = distance / 100 * y0

    return xStart + xL, yStart + yL


def startmotor(x, y, z):
    _twist = Twist()
    _twist.linear.x = 1 / 100 * x * 0.2
    _twist.linear.y = 1 / 100 * y * 0.2
    _twist.angular.z = 1 / 100 * z
    _motorPub.publish(_twist)


def run():
    print("starting roberta node...")
    rospy.sleep(0.3)

    driveForDistance(10, -10, 20)


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()
