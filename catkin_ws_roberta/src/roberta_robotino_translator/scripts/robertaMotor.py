#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

twist = Twist()
safety = Bool()

def twistCallback(data):
    global twist
    twist = data

def safetyModeCallback(data):
    global safety
    safety = data

def talker():
    rospy.init_node('robotino_go', anonymous=True)
    global twist, safety
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('cmd_vel_repeating', Twist, twistCallback)
    rospy.Subscriber('safety_mode', Bool, safetyModeCallback)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        print(safety.data, " bumper: ", rospy.wait_for_message("bumper", Bool), " Twist: ", twist)
        if safety.data and rospy.wait_for_message("bumper", Bool).data:
            twist = Twist()
        pub.publish(twist)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
