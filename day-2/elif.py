#elif statements allow you to add more than one else stement
print('what is your name? ')
name = input()
print('what is your age? ')
age = input()
# conveting string from the input into an intiger
age = int(str(age)) 
if name == 'jason':
    print('hi jason')
elif age == 43:
    print('you are ' + str(int(age))) # str(int(age))
elif age < 50:    
    print ('you are ' + str(int(age)))
elif name == 'bob':
    print('its really you ' + name)
# If all values are false, you can use an else statement.
else :
    print('Wow that is old.')

