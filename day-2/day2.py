# Day 2 code was used by following http://automatetheboringstuff.com/

##########################################################################
# Inputs and outputs 
# this is how to input a varible

print('What is your name? ')
# the name typed in will take on the my_name varible
my_name = input()
# output the response to the question
print('Hello ' + my_name)
##########################################################################
# Comparison operators 
# ==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
# !=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
# <>	If values of two operands are not equal, then condition becomes true.	(a <> b) is true. This is similar to != operator.
# >	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
# <	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
# >=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
# <=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.

# examples with varibles 
age = 43
age_next_year = 44
result = age == age_next_year
print (result)

age = 43
age_next_year = 56
result = age == age_next_year
print (result)

# the types of varibles for comparison must be the same type 
# this will always be false
age = 43
age_next_year = 'fifty six'
result = age == age_next_year
print (result)

age = 43
age_next_year = '43'
result = age == age_next_year
print (result)

# float values and intingers can be compaired 
age = 43
age_next_year = 43.5
result = age == age_next_year
print (result)
##########################################################################

##########################################################################
# boolan operators 
# and, or, not

# examples with varibles
age = 43
age_next_year = 53
result = age == 43 and age_next_year == 43
print (result)

age = 43
age_next_year = 53
result = age != 43 and age_next_year >= 43
print (result)

age = 43
age_next_year = 53
result = age != 43 or age_next_year >= 43
print (result)

##########################################################################
# if, else, and elif statements 
# elif statements allow you to add more than one else stement
name = 'jason'
if name == 'jason':
    print('hi ' + name)
else: 
    print('false')
print('done')

# example with using input
print('guess the password')
password = input()
if password == 'sowardfish':
    print('access granted')
else:
    print('your password was ' + password + '.'+ ' access denied')
print('done') 

# using elif
print('what is your name? ')
name = input()
age = 43
if name == 'jason':
    print('hi jason')
elif age == 43:
    print('you are' + age)
elif age < 50:
    print ('you are ' + age)
elif name == 'bob':
    print('its really you ' + name)

##########################################################################