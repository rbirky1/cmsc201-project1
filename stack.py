# File:     stack.py
# Author:   Rachael Birky
# Date:     04.16.12
# email:    rbirky1@umbc.edu
# Section:  02
#
# stack.py defines an abstract data type
#  and its methods
# a stack is a first-in, last-out list

# stack() creates a new stack
# Inputs: None
# Output: an empty stack
def stack():
    return []


# top() returns the item on top of the stack without popping
# Inputs: a stack
# Output: an item from the stack, if not empty
def top(aStack):
    if isEmpty(aStack):
        return None
    else:
        return aStack[-1]
 

# isEmpty() checks to see if stack is empty
# Inputs: a stack
# Output: True is stack is empty, False if not
def isEmpty(aStack):
    return len(aStack) == 0

# push() pushes the item passed in onto the stack passed.
# Inputs: a stack, an item to add
# Output: None
def push(aStack, item):
    aStack.append(item)

# pop() pops an item from the stack passed in and returns it.
# Input: a stack
# Output: the item at [-1] popped from the stack or
#         "Empty Stack" if the stack was empty
def pop(aStack):
    size = len(aStack)
    if size > 0:
        aStack.pop(-1)
    else:
        return "Empty Stack"
