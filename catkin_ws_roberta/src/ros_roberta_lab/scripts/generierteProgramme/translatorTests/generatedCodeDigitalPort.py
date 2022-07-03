#!/usr/bin/env python3

import rospy
import math, random
from geometry_msgs.msg import Twist
from ros_roberta_lab.msg import BooleanArray  # dieser Import
from std_msgs.msg import Bool

try:
    rospy.init_node('robotino_go', anonymous=True)
    _digitalPub = rospy.Publisher('set_digital_output', BooleanArray, queue_size=10) #beide globale variablesn
    _dqValues = [False for i in range(8)]
except Exception as e:
    raise

#zwei methoden
def _setDigital(pos, value):
    digitalReadings = BooleanArray()
    _dqValues[pos] = value
    digitalReadings.values = _dqValues
    _digitalPub.publish(digitalReadings)

def resetDigitalValues():
    _dqValues = [False for i in range(8)]

    digitalReadings = BooleanArray()
    digitalReadings.values = _dqValues
    _digitalPub.publish(digitalReadings)

def run():
    print("starting roberta node...")
    rospy.sleep(0.3)

    _setDigital(0, True)
    rospy.sleep(2000 / 1000)
    _setDigital(0, False)
    rospy.sleep(2000 / 1000)
    _setDigital(0, True)
    rospy.sleep(2000 / 1000)


def main():
    try:
        run()
    except Exception as e:
        raise
    finally:
        resetDigitalValues() #reset all ports
main()
