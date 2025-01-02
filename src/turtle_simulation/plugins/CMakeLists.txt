cmake_minimum_required(VERSION 3.10 FATAL_ERROR)
project(ControlPanelGUIPlugin)

# Find Gazebo GUI (gz-gui)
find_package(gz-gui8 REQUIRED)
find_package(gz-plugin2 REQUIRED)
find_package(gz-sim8 REQUIRED)
find_package(Qt5 REQUIRED COMPONENTS Widgets)


# Create the shared library for the plugin
add_library(ControlPanelGUIPlugin SHARED ControlPanelGUIPlugin.cc)

# Link the plugin to Gazebo GUI libraries
target_link_libraries(ControlPanelGUIPlugin gz-gui8::gz-gui8)
target_link_libraries(ControlPanelGUIPlugin gz-plugin2::gz-plugin2)
target_link_libraries(ControlPanelGUIPlugin gz-sim8::gz-sim8 Qt5::Widgets)

# Install the plugin to a location accessible by Gazebo
install(TARGETS ControlPanelGUIPlugin
        LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)
