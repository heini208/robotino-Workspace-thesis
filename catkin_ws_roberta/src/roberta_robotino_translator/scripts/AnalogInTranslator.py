#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray
from robotino_msgs.msg import AnalogReadings  # dieser Import

analogPub = rospy.Publisher('analog_inputs', Float32MultiArray, queue_size=10)
_speed = Twist()

def analogReadingsCallback(data):
    readings = Float32MultiArray()
    readings.data = data.values
    analogPub.publish(readings)

def talker():
    rospy.init_node('robotino_analog_in', anonymous=True)
    rospy.Subscriber('analog_readings', AnalogReadings, analogReadingsCallback)
    rospy.spin()
    if _speed.linear.x == _speed.linear.y == _speed.linear.z == 0:
        return

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass