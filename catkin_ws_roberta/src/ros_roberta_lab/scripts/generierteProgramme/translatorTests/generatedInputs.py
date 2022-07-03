#!/usr/bin/env python3

import rospy
import math, random
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

from ros_roberta_lab.msg import BooleanArray
from std_msgs.msg import Float32MultiArray

rospy.init_node('roberta', anonymous=True)

def run():
    print("starting roberta node...")
    rospy.sleep(0.3)

    digitalOne = rospy.wait_for_message("digital_inputs", BooleanArray).values[1]

    analogZero = rospy.wait_for_message("analog_inputs", Float32MultiArray).data[0]

    print("analog[0]= ", analogZero, " digital[0]=", digitalOne)

def main():
    try:
        run()
    except Exception as e:
        raise

main()
