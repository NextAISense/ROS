# ROS And Gazebo Integration

## Prerequisite to install:
ROS Installation

https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

Gazebo Installation

```bash
# Example running gz sim on Jazzy
export ROS_DISTRO=jazzy
sudo apt-get install ros-${ROS_DISTRO}-gz-tools-vendor ros-${ROS_DISTRO}-gz-sim-vendor
. /opt/ros/jazzy/setup.bash
gz sim --help
```
## For Building Integration

```bash
colcon build
```
```bash
source install/setup.bash
```
```bash
ros2 launch turtle_simulation turtle_gz.launch.py
```

