#elif statements allow you to add more than one else stement
# THIS NEEDS TO BE FIXED
print('what is your name? ')
name = input()
print('what is your age? ')
age = input()
if name == 'jason':
    print('hi jason')
elif age == 43:
    print('you are ' + str(int(age))) # str(int(age))
elif age < 50:
    print ('you are ' + str(int(age)))
elif name == 'bob':
    print('its really you ' + name)
print('done')