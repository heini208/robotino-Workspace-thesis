#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
from robotino_msgs.msg import AnalogReadings  # dieser Import

analogPub = rospy.Publisher('analog_inputs', Float32MultiArray, queue_size=10)


def analogReadingsCallback(data):
    readings = Float32MultiArray()
    readings.data = data.values
    analogPub.publish(readings)

def talker():
    rospy.init_node('robotino_analog_in', anonymous=True)
    rospy.Subscriber('analog_readings', AnalogReadings, analogReadingsCallback)
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass