#!/usr/bin/env python

# working on functions and variables

# print("hello world")

# This is a comment. We use it to take notes on our code. It makes note taking easy.

"""
This is a multi-line comment. Used for long important comments.
It's great for info dumping the stupidity I was thinking at the time.
It is used to write documentation for other readers.
"""

# y = mx + b
# y = 3x + 1

#this initializes x and y as variables in the code and sets their values to integer values.
x = 5
y = 3*x + 1
print(y)

#this is a varible with a string.
name = "Magic Ian"
print(name)
print(name + " is the Dungeon Master")
#types are not fixed in python
name = y + x
print(name)

# control / with make a comment or remove a comment on a line with content

# + is a function that has different definations based on if it's a str or an int.
is_beege_cool = False
# there are booleans.
# 0.5 is a float
# 1 is an interger
# "tonight" is a string
# there is also None a null type.
# floats and ints can be combined
# Many mixed type combinations break, but some have unexpected behavior
print( 1 + 0.5 )
# True = 1 and False = 0
print( 1 + True + False )

"""
This is a addition function made to take in two arguments and output their combination. 
def defines the function, everything before the : is the signature Inputs are seperated by commas. 
The colon signals the start of the body.
return is the output of the function.
"""

def add(a,b):
    return a+b

print(add( 3, 5))
#this function still has the same behavior of the '+' opperator
print(add( "Not ", "a number"))
