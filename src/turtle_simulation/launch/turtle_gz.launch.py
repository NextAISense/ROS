from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # Path to the turtle model (update this with your actual model location)
    model_file = PathJoinSubstitution([FindPackageShare('turtle_simulation'), 'models/turtlebot/model.sdf'])
    print("MODEL_FILE:", model_file.__dict__)
    return LaunchDescription([
        # Start the Gazebo simulator with the default world file
        # ExecuteProcess(
        #     cmd=['gz', 'sim'],
        #     output='screen'
        # ),
        
        # Spawn the turtle model into the Gazebo world
        ExecuteProcess(
            cmd=['gz', 'sim', model_file],
            output='screen'
        ),
        
        # Start the ROS 2 node that will control the turtle
        Node(
            package='turtle_simulation',  # Your ROS package
            executable='turtle_control',  # The Python node that controls the robot
            name='turtle_control',        # The node's name
            output='screen',              # Display node output on the screen
        ),
    ])
