cmake_minimum_required(VERSION 3.5)
project(joystick_controller)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# Install Python scripts
install(PROGRAMS
  scripts/joystick_controller_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# Define the executables
ament_python_install_package(${PROJECT_NAME})

ament_package()
