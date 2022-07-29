#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8MultiArray
from robotino_msgs.msg import DigitalReadings  # dieser Import

digitalPub = rospy.Publisher('set_digital_values', DigitalReadings, queue_size=10)


def BooleanArrayCallback(data):
    digitalReadings = DigitalReadings()
    digitalReadings.stamp = rospy.Time.now()
    digitalReadings.values = list(map(bool,data.data))
    digitalPub.publish(digitalReadings)

def listener():
    rospy.init_node('robotino_digital_out', anonymous=True)
    rospy.Subscriber('set_digital_output', Int8MultiArray, BooleanArrayCallback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
