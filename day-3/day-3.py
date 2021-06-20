############################################################################
#  While loops 
###########################################################################
# Simple example 
number = 0 
while number < 5:
    print('example')
    number = number + 1

# Adding additonal code to execute after the loop is closed 
# this is a foundation for input validation
name = ''
while name !='your name':
    print('Please type your name')
    name = input()
print('Thank you') # if you do not type in "your name", the loop will continue.
                   # once you type in "your name" the loop will end and the code will continue.

