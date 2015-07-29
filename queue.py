# File:     queue.py
# Author:   Rachael Birky
# Date:     04.16.12
# email:    rbirky1@umbc.edu
# Section:  02
#
# queue.py defines an abstract data type
#  and its methods
# a queue is a first-in, first-out list

# queue() creates an empty queue
# Inputs:  none
# Outputs: an empty queue
def queue():
    return []

# enqueue() adds a given item to the given queue
# Inputs:  a queue, an item to be added
# Outputs: None
def enqueue(aQueue, item):
    aQueue.append(item)


# front() retrieves the item at the head of the queue
#  without deleting it!
# Inputs:  a queue
# Outputs: the first item, if not an empty queue
def front(aQueue):
    if isEmpty(aQueue):
        return "Empty Queue"
    else:
        return aQueue[0]

# isEmpty(aQueue) checks to see if queue is empty
# Inputs: aQueue, a queue
# Output: True is queue is empty, False if not
def isEmpty(aQueue):
    return len(aQueue) == 0

# dequeue() retrieves and deletes the first item
#  of the queue
# Inputs:  a queue
# Outputs: the first item, if not an empty queue
def dequeue(aQueue):
    if isEmpty(aQueue):
        return "Empty Queue"
    else:
        aQueue.pop()
