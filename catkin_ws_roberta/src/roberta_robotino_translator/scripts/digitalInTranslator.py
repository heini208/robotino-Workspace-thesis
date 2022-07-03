#!/usr/bin/env python3
# license removed for brevity
import rospy
from robotino_test.msg import BooleanArray
from robotino_msgs.msg import DigitalReadings

digitalPub = rospy.Publisher('digital_inputs', BooleanArray, queue_size=10)


def digitalReadingsCallback(data):
    digitalPub.publish(data.values)

def talker():
    rospy.init_node('robotino_digital_in', anonymous=True)
    rospy.Subscriber('digital_readings', DigitalReadings, digitalReadingsCallback)
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass