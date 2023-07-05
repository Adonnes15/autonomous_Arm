#!/bin/env python3
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from math import sin

class commander():
    def __init__(self):
        rospy.init_node('commander')
        rospy.Subscriber("/manipulator/joint_states",JointState,self.callback)
        self.pub=rospy.Publisher("/manipulator/joint2_position_controller/command",Float64,queue_size=1)
        self.list=[1,-1,1.57,-1.57,0]
        self.i=1
        rospy.spin()

    def callback(self,msg):
        goal=self.list[self.i]
        position=msg.position[1]
        print(position)
        self.pub.publish(goal)
        if position-goal<=0.01 and position-goal>=-0.01:
            self.i+=1

    


if __name__=='__main__':
    obj=commander()