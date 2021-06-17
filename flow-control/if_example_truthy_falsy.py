print('Enter a name.')
name = input()
if name != '':
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')
""""
# 0 is falsy, all others are truthy.
# 0.0 is falsy, all others are truthy.
# condition had to be reinforced with != not equal to comparison operator
# because it would accept a blank string aka falsy value condition
# falsy value condition is same as false Boolean value
# To check which values are truthy or falsy, pass them to the bool() function
"""
