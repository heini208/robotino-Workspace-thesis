#!/usr/bin/env python3
import rospy
from ros_roberta_lab.msg import BooleanArray
from robotino_msgs.msg import DigitalReadings  # dieser Import

digitalPub = rospy.Publisher('set_digital_values', DigitalReadings, queue_size=10)


def BooleanArrayCallback(data):
    digitalReadings = DigitalReadings()
    digitalReadings.stamp = rospy.Time.now()
    digitalReadings.values = data.values
    print("Forwarding: ", digitalReadings.values)
    digitalPub.publish(digitalReadings)

def listener():
    rospy.init_node('robotino_digital_out', anonymous=True)
    rospy.Subscriber('set_digital_output', BooleanArray, BooleanArrayCallback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass