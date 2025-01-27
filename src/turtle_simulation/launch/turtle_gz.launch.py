from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # Path to the turtle model (update this with your actual model location)
    model_file = PathJoinSubstitution([FindPackageShare('turtle_simulation'), 'models/turtlebot/model.sdf'])
    config_file = PathJoinSubstitution([FindPackageShare('turtle_simulation'), 'models/turtlebot/CustomClient.config'])
    print("MODEL_FILE:", model_file.__dict__)
    return LaunchDescription([
        # Start the Gazebo simulator with the default world file
        # ExecuteProcess(
        #     cmd=['gz', 'sim'],
        #     output='screen'
        # ),
        
        # Spawn the turtle model into the Gazebo world
        ExecuteProcess(
            cmd=['gz', 'sim', model_file, '--gui-config', config_file],
            output='screen'
        ),
        
        # Start the ROS 2 node that will control the turtle
        # Node(
        #     package='turtle_simulation',  # Your ROS package
        #     executable='turtle_control',  # The Python node that controls the robot
        #     name='turtle_control',        # The node's name
        #     output='screen',              # Display node output on the screen
        # ),
        # Add the ROS-Gazebo bridge for the /cmd_vel topic
        Node(
            package='ros_gz_bridge', 
            executable='parameter_bridge', 
            name='ros_gz_bridge', 
            arguments=['/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'], 
            output='screen'
        ),
        #Add Teleop Control Bar node
        # Node(
        #     package='turtle_simulation',  # Update to your package name
        #     executable='teleop_control',  # Ensure this matches the entry in `setup.py`
        #     name='teleop_control',
        #     output='screen',
        # ),
        #Inbuilt GUI of the control panel
        # Node(
        #     package='turtle_simulation',
        #     executable='control_panel',
        #     name='control_panel',
        #     output='screen',
        # ),

    ])
