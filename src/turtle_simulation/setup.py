from setuptools import find_packages, setup

package_name = 'turtle_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include the launch directory
        ('share/' + package_name + '/launch', ['launch/turtle_gz.launch.py']),
        ('share/' + package_name + '/models/turtlebot', ['models/turtlebot/Car_Bot.urdf']),
        ('share/' + package_name + '/models/turtlebot', ['models/turtlebot/model.config']),
        ('share/' + package_name + '/models/turtlebot', ['models/turtlebot/CustomClient.config']),
        ('share/' + package_name + '/models/turtlebot/meshes', ['models/turtlebot/meshes/CAR_BODY.stl']),
        ('share/' + package_name + '/models/turtlebot/meshes', ['models/turtlebot/meshes/wheel1.STL']),
        ('share/' + package_name + '/models/turtlebot/meshes', ['models/turtlebot/meshes/wheel2.STL']),
        ('share/' + package_name + '/models/turtlebot/meshes', ['models/turtlebot/meshes/wheel3.STL']),
        ('share/' + package_name + '/models/turtlebot/meshes', ['models/turtlebot/meshes/wheel4.STL']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zahid',
    maintainer_email='zahid@nextaisense.com',
    description='Turtle simulation with ROS 2 and Gazebo.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ #'turtle_control = turtle_simulation.turtle_control:main',
                            # 'teleop_control = turtle_simulation.teleop_control:main',
                            #'control_panel = turtle_simulation.control_panel:main',
        ],
    },
)
