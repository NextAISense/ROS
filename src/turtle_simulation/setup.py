from setuptools import find_packages, setup

package_name = 'turtle_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include the launch directory
        ('share/' + package_name + '/launch', ['launch/turtle_gz.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zahid',
    maintainer_email='zahid@nextaisense.com',
    description='Turtle simulation with ROS 2 and Gazebo.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['turtle_control = turtle_simulation.turtle_control:main',
        ],
    },
)
