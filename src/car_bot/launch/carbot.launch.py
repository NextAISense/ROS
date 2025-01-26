from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # Path to the carbot model (update this with your actual model location)
    model_file = PathJoinSubstitution([FindPackageShare('car_bot'), 'model/car_robot.urdf'])
    planet_file =  PathJoinSubstitution([FindPackageShare('car_bot'), 'model/world.sdf'])
    config_file = PathJoinSubstitution([FindPackageShare('car_bot'), 'model/CustomGzInterface.config'])
    print("MODEL_FILE:", model_file.__dict__)
    return LaunchDescription([
        # Start gazebo using the planet environment
        ExecuteProcess(
            cmd=['gz', 'sim', planet_file, '--gui-config', config_file],
            output='screen'
        ),
        
        #Spawn the urdf model file
        Node(
            package="ros_gz_sim",
            executable="create",
            name="spawn_car_robot",
            arguments=["-file", model_file, "-name", "car_robot"],
            output="screen"
        ),
       
        # Add the ROS-Gazebo bridge for the /cmd_vel topic
        Node(
            package='ros_gz_bridge', 
            executable='parameter_bridge', 
            name='ros_gz_bridge', 
            arguments=['/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'],
            output='screen'
        ),

        # Node(
        #     package='ros_gz_bridge',
        #     executable='parameter_bridge',
        #     name='ros_gz_bridge_cmd_steering',
        #     arguments=['/cmd_steering@std_msgs/msg/Float64@gz.msgs.Double'],
        #     output='screen',
        # ),
        # Steering control node
        # Node(
        #     package='steering_controller',
        #     executable='steering_node',
        #     name='steering_controller',
        #     output='screen'
        # ),
        
    ])
