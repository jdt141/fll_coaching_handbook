


# Welcome to coding for First Lego League, and I'll be your host, Johnny5. 
# Your human coach should be able to give you the heart of our robot, the HUB. 

# Three fun facts about the hub: 
# 1) This is the "brain" of the robot. All the software you write will run on the HUB
# 2) The HUB has 6 "ports" that you plug things into, labeled A through F
# 3) The HUB also has some special sensors inside of it (a gyro), 
# which we'll explore in the future. 


# If you've never written software before, welcome!! These green lines with
# the hashtag at the start are what is called a "comment" and that means
# that you can write anything you want after the hashtag, like:  
# BLORK!!!
# and the HUB will simply ignore that text.

# Fun fact 4: comments are great for writing things down about your code so that you
# remember what the code does later. ** You humans are SOOO forgetful *** 

# These next lines (that aren't green) is our first actual lines of real code!! 
# They basically tell the HUB how to start up. You'll need to do this at
# the start of every piece of software you write for lego. 

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# In this lesson, we're going to connect up a motor and get it to spin!! WheEeEEE!!! 
# It's your job to tell the HUB what port you've connected your motor. 

# I'll give you a hint! It looks something like this next line
# What do you think you'll have to change in this next line of code 
# to tell the HUB what port you've connected the motor to? 
# Hint - Fun Fact #2 can help you answer this question

myMotor = Motor(Port.A) 

# Check with your human coach to make sure you've set up your motor correctly!
# now it's time to spin! spin! spin!! 
# I LOOOOVE to spin. I just want to spin all the time.

# Here's the simplest way to do that:

while True:
    #spin me around!
    mySpeed = 1000
    myMotor.run(speed = mySpeed)
    print("I love to spin!")

# Question 1: Can you change the code to make me spin more slowly?
# Write down what you'd change here and try it!! (Coaches scroll down for the answer)
#
#
#
# Question 2: Can you change the code to make me spin in the other direction?
# Write down what you'd change here and try it!!
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
# Answer 1: Change the mySpeed number to anything less than 1000. 
# Answer 2: Change the mySpeed number to a negative number (-1000 to -1) to
# get the motor to spin in the opposite direction

