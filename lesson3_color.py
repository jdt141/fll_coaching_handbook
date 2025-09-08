# Welcome back! Johnny5 here. I hope you had fun learning about two motors. 
# Did you get your robot to spin? to drive straight? 

# BUT... we have a new special super fun thing to play with in this lesson
# The
# CoLoR sensor!!!! 

# super useful for things like.. snacks! Did I mention I like snacks? 

# ok so we have this very important but kind of boring code
# i haven't talked much about it, but there's really some interesting things
# going on here

# this important code uses the word `import` a lot. 
# that means it's bringing in a bunch of other code that someone else
# wrote that YOU can use to help YOU do what YOU want without having to
# worry about a bunch of details. (like how a motor works)

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# the only reason we can use PrimeHub is because it was imported on line 19! 
hub = PrimeHub()

# so, cool to know. If you take a close look at Line 20, we have things like 
# Motor
# ColorSensor
# and a bunch of other FUUUUUN stuff we can play with. 

# let's start with something new - the color sensor!! yahhhh!!!  
# Question 1 - what do you need to change about this line to make sure your
# HUB knows about the Color Sensor? 
myColorSensor = ColorSensor(Port.B)

# Now that you have your HUB all set up, we can start to use the color sensor
# To start we're just going to see what kinds of colors the sensor can see! 
# go get a bunch of legos of different colors from the bin. Then we can start
# to learn about what the sensor can do. 


# did you get those legos yet? noooo? What are you waiting for?!?! 
# if you did, great. Let's take a look at this code! 

# forever
while True:
    # read the color from the sensor
    color = myColorSensor.color()
    # print the color out to the console (the bottom part of this window)
    print(color)
    # wait a little bit of time, just so you can read the output
    wait(100)

# Question 1 - what did you notice when you pointed the sensor at the air?
# Question 2 - what did you notice when you pointed the sensor at some legos? 
# Was the color sensor always right? 

#
#
#

#
#
#
#
##
#
#
#
##
#
#
#
## keep scrolling! 
#
#
#
##
#
#
#
##
#
#
#
##
#
#
#
##
#
#
#
## Getting close!! 
#
#
#
##
#
# Answer 1: It should look something like, but without the hashtag
# myMotor2 = Motor(Port.B)


# Answer 2: Duplicate 
#    myMotor.run(speed = mySpeed)
# by changing to the variable you assigned in Answer1. (In this example I used myMotor2)
# It should look like
# myMotor2.run(speed = mySpeed)


