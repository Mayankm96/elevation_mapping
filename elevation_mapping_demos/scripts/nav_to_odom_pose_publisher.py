#!/usr/bin/env python
import rospy
import nav_msgs.msg
import geometry_msgs.msg
import std_msgs
import tf

def callback(newPose):
    global publisher

    pose = geometry_msgs.msg.PoseWithCovarianceStamped()
    # header message
    pose.header.stamp = newPose.header.stamp
    pose.header.frame_id = "zed_center"
    # pose message
    pose.pose.pose.position.x = newPose.pose.pose.position.x
    pose.pose.pose.position.y = newPose.pose.pose.position.y
    pose.pose.pose.position.z = newPose.pose.pose.position.z
    pose.pose.pose.orientation.x = newPose.pose.pose.orientation.x
    pose.pose.pose.orientation.y = newPose.pose.pose.orientation.y
    pose.pose.pose.orientation.z = newPose.pose.pose.orientation.z
    pose.pose.pose.orientation.w = newPose.pose.pose.orientation.w
    # covariance message
    pose.pose.covariance = newPose.pose.covariance

    publisher.publish(pose)

#Main function initializes node and subscribers and starts the ROS loop
def main_program():
    global publisher
    rospy.init_node('nav_to_odom_pose_publisher')

    subscriber = rospy.Subscriber("/odom", nav_msgs.msg.Odometry, callback)
    publisher = rospy.Publisher('/pose_g', geometry_msgs.msg.PoseWithCovarianceStamped, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        main_program()
    except rospy.ROSInterruptException: pass
