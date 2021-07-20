# While Loop: A while loop will continue to run while the condition is true.
# Break and Continue Statements 

# Break statements causes the execution to immediately leave the look without rechecking the condition
name = ''
while True:
    print("Please type in your name.")
    name = input()
    if name == "your name":
        break ######################
print("Thank you!")


# Continue statements causes the execution to immediately jump back to the start of the loop and recheck the condition
spam = 0 
while spam < 5:
    spam = spam + 1
    if spam == 3:
       continue  #################
    print ('spam is ' + str(spam)) # here, I converted the int spam to a string
