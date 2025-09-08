# Johnny 5 again. Did you think it was going to be someone else?

# now that we've learned about motors and colors... we get to learn about
# something very important in all of robotics!! 

# snacks. it's all about the snacks!! 

# (I hope your adult coaches are laughing!!)
# It's not ALLL about the snacks (but I do love them)
# We're going to learn about one of the most important things
# it's how pretty much all robots work! 
# It's called
# Sense
# Plan
# Act

# All robots do this in a Loop over and over again to do something in the world
# so guess what? 
# we know how to sense - with a color sensor!! 
# and we know how to act - with our motors. 
# What connects the two things? 
# (no, it's not the snacks)

# the plan!! yes, the plan is super important. It let's you take sensor inputs
# and then do something fun with them!! So in this lesson, we're going to create
# a plan! (a plan to get snacks, of course!!)

# so to start we're going to pull in this code again. 
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# and we're going to set up our hub. 
hub = PrimeHub()

# and we'll set up both our color sensor and our motors
myColorSensor = ColorSensor(Port.B)
myMotor = Motor(Port.A)
myMotor2 = Motor(Port.C)

# forever
while True:
    # First, we SENSE!! 
    color = myColorSensor.color()
    # print the color out to the console (the bottom part of this window)
    print(color)

    # Next we have to create a plan
    # Here, I want us to do something simple and fun
    # (We'll get to the snacks later)

    # if the color we see is YELLOW, I want us to go slow
    # for every other color, I want us to go FAST. 

    # to do that, we'll create a place to hold our planned speed 
    # This is called a variable

    plannedSpeed = 0

    # next, we need to set the speed. to do that we need some basic operations
    # called if and else. This lets us adjust our plannedSpeed. 

    if (color == Color.YELLOW) or (color == Color.BLUE): 
        # go fast
        plannedSpeed =  # Question 1A - what goes here?
    else: 
        #go slow
        plannedSpeed =  # Question 1B - what goes here? 


    # finally we ACT. The way we act on the world is through our motors. 
    myMotor.run(speed=plannedSpeed)
    myMotor2.run(speed=plannedSpeed)


# Question 2: Could you change this code to make it respond to Color.BLUE? 
# Question 3: Could you change this code to make it respond to Color.BLUE OR Color.YELLOW? 

# Congrats! You've learned all about sense, plan, and act!! 
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
# Answer2 
#
#    if color == Color.RED: 
#        # go fast
#        plannedSpeed = # Question 1A - what goes here? 
#    else: 
#        #go slow
#        plannedSpeed = # Question 1B - what goes here? 

# Answer3  - there are several correct answers here, this is one example
#
 #   if (color == Color.YELLOW) or (color == Color.BLUE): 
 #       # go fast
 #       plannedSpeed = 1000 # Question 1A - what goes here?
 #   else: 
        #go slow
 #       plannedSpeed = 400 # Question 1B - what goes here? 
#
#
#
