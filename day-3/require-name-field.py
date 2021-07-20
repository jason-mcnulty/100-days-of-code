###########################################################################
# This program will require a name to be used as the input. 
# The challenge is not to allow any numbers 0-9
###########################################################################

# Adding additonal code to execute after the loop is closed 
# this is a foundation for input validation
name = ''
while name !='your name':
    print('Please type your name')
    name = input()
print('Thank you') # if you do not type in "your name", the loop will continue.
                   # once you type in "your name" the loop will end and the code will continue.


# This is a different way of performing the while loop using a "break" statement 
name = ''
while True:
    print("Please type in your name.")
    name = input()
    if name == "your name":
        break
print("Thank you!")