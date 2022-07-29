#!/usr/bin/env python3
# license removed for brevity
import rospy
import numpy as np
from std_msgs.msg import Int8MultiArray
from robotino_msgs.msg import DigitalReadings

digitalPub = rospy.Publisher('digital_inputs', Int8MultiArray, queue_size=10)


def digitalReadingsCallback(data):
    intArray = Int8MultiArray()		
    intArray.data = np.uint8(data.values)
    digitalPub.publish(intArray)

def talker():
    rospy.init_node('robotino_digital_in', anonymous=True)
    rospy.Subscriber('digital_readings', DigitalReadings, digitalReadingsCallback)
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
