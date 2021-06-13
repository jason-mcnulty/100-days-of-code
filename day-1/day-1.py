# Day 1 
# Back to basics, a lot of this was inspired from https://www.w3schools.com/python/default.asp
# I also used code by following http://automatetheboringstuff.com/

###########################################################################
# Working with variables
x = "Five"
y = "John"
print(x)
print(y)

# Many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. 
# This is called unpacking
fruits = ["apple", "banana", "cherry"]
# At this point fruits == ["apple", "banana", "cherry"]
x, y, z = fruits
# Each letter will become a varible for each item in the list.
print(x)
print(y)
print(z)
###########################################################################

###########################################################################
# Concatenation of strings
x = "Five"
y = "John"
print(x)
print(y)
# Here, double quotes are used for o'clock because if single quotes where used, 
# the 'o would break up the string.
print ('Hello ' + y + ', ' + 'the time is ' + x + " o'clock")

# A seperate varable can be created to perform the concatenation 
x = "sunny"
y = " day"
z = x+y
print(x)
print(y)
print ('It is such a' + z)

# Using string replication 
name = 'John '
print (name * 3)

###########################################################################
# Data types
# Intigers == int == 3
# Float == float == 3.4 
# String == str == 'cat'

# Convert x from int to a string
x = 5
y = "Five"
z = "John"
x = str(x)
print ('Hello ' + z + ', ' + 'the time is ' + x + " o'clock")

# Convert x from float to a string
x = 5.5
y = "Five"
z = "John"
x = str(x)
print ('Hello ' + z + ', ' + 'the time is ' + x + " o'clock")
###########################################################################

###########################################################################
# Math - Expressions
# My final goal is to create a web app that I will use to determine the # of shares to purchase
# given the amount of money to spend

# simple math concatenation of intigers
# Adding 
x = 5
y = 10
print(x + y)

# Division
x = 500 # price per share
y = 200000 # amount of money for purchase
print (y / x) # numner of shares you can buy

# Multiplication
x = 2
y = 10
print (x * y)

# Order of operiations are used 
# Simple
x = 2
y = 10
z = 6
print (x + y * z)

# More complex
x = 2
y = 10
z = 6
print ((x + y) * z)

# Even more complex 
a = 20
w = 10
x = 2
y = 10
z = 6
print ((a - w ) * ((x + y ) / (z - y)))
###########################################################################
