#!/usr/bin/env python3
import rospy
import math, random
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from robotino_msgs.srv import ResetOdometry

rospy.init_node('robotino_go', anonymous=True)
_motorPub = rospy.Publisher('cmd_vel_repeating', Twist, queue_size=10)


def _getOrientation():
    yaw_z = 2 * math.acos(rospy.wait_for_message("odom", Odometry).pose.pose.orientation.w) #TODO DELETED * 180 / math.pi
    if rospy.wait_for_message("odom", Odometry).pose.pose.orientation.z < 0:
        yaw_z *= -1
    return yaw_z

def _driveToPosition(xTarget, yTarget, speed):
    firstPositionX = rospy.wait_for_message("odom", Odometry).pose.pose.position.x * 100
    firstPositionY = rospy.wait_for_message("odom", Odometry).pose.pose.position.y * 100
    while True:
        speedX, speedY = _getDirection(xTarget, yTarget, speed)
        _setSpeedOmnidrive(speedX, speedY, 0)

        xPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.x * 100
        yPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.y * 100
        if firstPositionX >= xTarget >= xPos or firstPositionX < xTarget <= xPos:
            if firstPositionY >= yTarget >= yPos or firstPositionY < yTarget <= yPos:
                _setSpeedOmnidrive(0, 0, 0)
                break
    rospy.Rate(10).sleep()

def _getDirection(xTarget, yTarget, speed):
    vectorX = xTarget - rospy.wait_for_message("odom", Odometry).pose.pose.position.x * 100
    vectorY = yTarget - rospy.wait_for_message("odom", Odometry).pose.pose.position.y * 100
    absV = math.sqrt(math.pow(vectorX, 2) + math.pow(vectorY, 2))
    maxSpeedX = (vectorX / absV)
    maxSpeedY = (vectorY / absV)
    angle = -_getOrientation() #* (math.pi / 180)
    rotatedX = (math.cos(angle) * maxSpeedX) - (math.sin(angle) * maxSpeedY)
    rotatedY = (math.sin(angle) * maxSpeedX + math.cos(angle) * maxSpeedY)
    return rotatedX * speed, rotatedY * speed


def _setSpeedOmnidrive(x, y, z):
    twist = Twist()
    twist.linear.x = (1 / 100 * x) * 0.2
    twist.linear.y = (1 / 100 * y) * 0.2
    twist.angular.z = 1 / 100 * z
    _motorPub.publish(twist)


def run():
    print("starting roberta node...")
    rospy.ServiceProxy('reset_odometry', ResetOdometry)(0, 0, 0)
    rospy.sleep(0.3)

    _driveToPosition(-20, 0, 50)
    rospy.sleep(500 / 1000)
    _setSpeedOmnidrive(0, 0, -30)
    rospy.sleep(500 / 1000)
    _setSpeedOmnidrive(0, 0, 0)
    _driveToPosition(0, 0, 50)


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        _motorPub.publish(Twist())


main()


#def _driveToPosition(xTarget, yTarget, speed):
#    oldOrientation = _getOrientation()
 #   while True:
  #      speedX, speedY = _getDirection(xTarget, yTarget, speed)
   #     if oldOrientation - _getOrientation() >= (math.pi/2) /2:
    #        _setSpeedOmnidrive(speedX, speedY, 0)
     #   else:
      #      _setSpeedOmnidrive(speedX, speedY, 50)
       #     print(speedX)


#        xPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.x * 100
 #       yPos = rospy.wait_for_message("odom", Odometry).pose.pose.position.y * 100
  #      tolerance = 5
   #     differenceX = abs(xTarget - xPos)
    #    differenceY = abs(yTarget - yPos)
     #   if differenceX <= tolerance:
      #      if differenceY <= tolerance:
       #         _setSpeedOmnidrive(0, 0, 0)
        #        break
    #rospy.Rate(10).sleep()