from setuptools import find_packages, setup

package_name = 'car_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include the launch and model directories
            ('share/' + package_name + '/launch', ['launch/carbot.launch.py']),
            ('share/' + package_name + '/model', ['model/car_robot.urdf']),
            ('share/' + package_name + '/model', ['model/world.sdf']),
            ('share/' + package_name + '/model', ['model/model.config']),
            ('share/' + package_name + '/model', ['model/CustomGzInterface.config']),
            ('share/' + package_name + '/model/meshes', ['model/meshes/base_link.STL']),
            ('share/' + package_name + '/model/meshes', ['model/meshes/wheel1.STL']),
            ('share/' + package_name + '/model/meshes', ['model/meshes/wheel2.STL']),
            ('share/' + package_name + '/model/meshes', ['model/meshes/wheel3.STL']),
            ('share/' + package_name + '/model/meshes', ['model/meshes/wheel4.STL']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zahid',
    maintainer_email='dewan.zahid365@gmail.com',
    description='ROS_GAZEBO Integrated Project',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
