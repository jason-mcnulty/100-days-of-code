# a global varible can be set outside of a function. 
# a local varible is one inside a function. 
# the same varible name can be set global and localy without overwritting each other. 

##########################################################################################
spam = 42 # global varible 
def eggs():
    spam = 43 # local varible
##########################################################################################

##########################################################################################
# if you want to assign a global varible from inside a function (local varible)
def spam():
    global eggs # add the word global within the local varible
    eggs = "Hello"
    print(eggs)

eggs = 42 # this varible will not be used as the global key word was applied in the local scope
spam()
print(eggs)
##########################################################################################