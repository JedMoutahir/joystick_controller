# ROS 2 Joystick Controller

## Author
[Moutahir Jed](https://github.com/JedMoutahir)


### Task

Create a small ros package with a node that will receive the joystick data and
send corresponding commands to the simulated robot.

### Starting the simulation

first starting the simulated robot :

``` cd /cs-share/pradalier/CoppeliaSim ```

then

``` ./coppeliaSim.sh ```

and navigate to the scene in

``` /cs-share/pradalier/ros2_ws/src/scenes ```

and open the scene called 

``` rosControlKinect.ttt ```

You should see this : 

![Alt text](HW1/initial_position.png?raw=true "Scene")

You can now start the simulation using the play button.

### Starting the joystick node

Open a terminal and type

``` ros2 run joy joy_node ```

if it isn't visible with

``` ros2 run joy joy_enumerate_devices ```

make sure it is plugged in correctly

### Starting the controller node

After building the package you should be able to start it with

``` ros2 run joystick_controller test_joystick_node ```

If you view the Graph you should see this

``` rqt_graph ```

![Alt text](HW1/rosgraph.png?raw=true "Graph")

you can now control the robot using the controller

![Alt text](HW1/after_inputs.png?raw=true "Scene2")
