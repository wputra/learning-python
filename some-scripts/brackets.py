#!/usr/bin/python3

test = "(((())(())()((()))))(((())(())()((())))))((((())(())()((()))))(((())(())()((()))))()((((()))))"

# this will use smallest resources
def check(string):
    c = 0
    for i in string:
        if i == '(':
            c += 1
        else:
            c -= 1
    return c

if test.count('(') != test.count(')'): # must be same
    print('something wrong')

if test[0] == ')' or test[-1] == '(': # check first and last element
    print('something wrong 1')
elif len(test) % 2 != 0: # must be even
    print('something wrong 2')
elif check(test) != 0: # must be 0
    print('something wrong 3')
else:
    print('true')
