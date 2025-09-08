# Welcome back! Johnny5 here. I hope you had fun learning about a motor. 
# I'm a little dizzy!! 

# Hopefully your human coach is NICE and actually gave you TWO motors. 
# In this lesson, we need two motors to make our robot GOOOOOO. 
# I could probably do it with one, but....
# it's just way too hard to get around that way. 


# SO!!  Who is ready to try using TWO motors?! 
# Great!! Let's go. 

# first thing is first - we need all this fun initialization code: 
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Now remember. This is the code we used last time.  
# We need to 1) copy and 2) change this line of code to add a second line of code
# to talk to the other motor. 
# Question 1: What new line of code do you need to add here to tell your hub 
# about the second motor? hmmm??

myMotor = Motor(Port.A) 
# Coaches scroll to the bottom for an answer 


while True:
    #spin me around!
    mySpeed = 1000
    myMotor.run(speed = mySpeed)
    print("I love to spin!")
     # Question 2. What line of code above do you need to copy and modify 
     # and add to make BOTH motors spin?



# Question 3: Now that you can spin two motors, not just one...
# can you do some building of a simple robot? Add some things like
# Wheels
# A base? 
# Maybe some snacks? Johnny 5 loves snacks!! 

# once you have your robot built and you've made the changes above.. 
# Can you get your robot to spin? Can you get it to drive straight?
# Use what you learned from lesson 1 (Question 2) to get your robot to do
# these fun moves!! 





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


