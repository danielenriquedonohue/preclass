#link to learning https://www.udemy.com/course/pythonforbeginnersintro/learn/lecture/8256980#overview

# #4 Variables and multiple assignment
print('hello world')

import sys; #import the functions that tie into the operating system

# print the system install information 
print('Print %s on %s' % (sys.version, sys.platform))
#this print fucntion passes uses placeholders to pass in the information from the installed python version and the installed python platform. 
# The % sign after the tells the print function that the comma separated values within the parentases are to be passed into the print function and used as a first come first use basis

age = 34
# when using the python interpretor typing the name of a variable will produce the contents of that variable, but only with the interpretor. 

sentence = "Hola amigo, My name is Kyle"

sarah = 16
bob = 21
mike = 17

# we can assign values to variables in a comma separated fasion, sarah, bob, mike = 16,21,17 instead of having to declare them and assign them independantly

# also, we can re-assign a value to a variable when we call it later in the script
# for example

print(age)

kyle = 34
age = kyle +1
print('age is now equal to kyle, which is 34 + 1 =',age)
print(age)
print(kyle)
