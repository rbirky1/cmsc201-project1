from Airplane import *
from stack import *
from queue import *

FILE_ONE = "runway1.txt"
FILE_TWO = "runway2.txt"
FILE_THREE = "runway3.txt"
WAIT_TIME = 5

# printGreeting() displays a greeting & explanation of the program to the user
# input:  None
# output: None
def printGreeting():
    print "\nWelcome to the BWI Snowmagedon Simulator!! This program analyzes\
\nthree sets of data representing airplanes, and determines the order of\
\ntake off in the event of poor weather using priority algorithms"


# makeRunway() loops through text files and saves information in stacks
# input:  None (files are opened with I/O inside function)
# output: runway 1, 2, and 3 as stacks, reversed order
def makeRunway(inFile):
    runway = stack()

    # Open file to read 
    runwayFile = open(inFile, "r")
    for line in runwayFile:
        # Make a plane of each line
        thisPlane = makePlane(line)
        # Place plane in stack
        push(runway, thisPlane)
    runwayFile.close()
    
    return runway


# makePlane() creates an instance of a plane
# input:  line of text in runway file
# output: airplane object
def makePlane(line):
    # Eliminiate white space and separate values
    line = line.strip().split()
    # Create instance of Airplane with values
    thisPlane = Airplane(line[0], line[1])

    return thisPlane

# makeQueue() places airplanes in a queue by priority
# input:  runway 1, 2, 3 stack
# output: runway4 queue
def makeQueue(runway1, runway2, runway3):
    planeQueue = queue()

    # Loop as long as there are planes left in any of the runways
    while (not isEmpty(runway1) or not isEmpty(runway2) or not isEmpty(runway3)):
        # Call nextPlance to find priority plane
        nextPlane = getNext(runway1, runway2, runway3)
        # Add priority plane to queue
        enqueue(planeQueue, nextPlane)
        
    return planeQueue


# getNext() compares the top planes in the stacks and returns highest priority
# input:  runway 1, 2, 3 stack
# output: airplane  with highest priority
def getNext(runway1, runway2, runway3):
    # Get first plane in each runway, or if empty, None
    plane1 = top(runway1)
    plane2 = top(runway2)
    plane3 = top(runway3)

    # If there is a plane, assign passenger count to variable
    if plane1 == None:
        num1 = 0
    else:
        num1 = plane1.getNumOfPassengers()
    if plane2 == None:
        num2 = 0
    else:
        num2 = plane2.getNumOfPassengers()
    if plane3 == None:
        num3 = 0
    else:
        num3 = plane3.getNumOfPassengers()

    # Find largest passenger count using a list and max() operation
    numList = [num1, num2, num3]
    maxNum = max(numList)

    # Find plane that correlates with largest passenger count
    #  this plane is returned to be added to queue
    if maxNum == num1:
        nextPlane = runway1.pop()
    if maxNum == num2:
        nextPlane = runway2.pop()
    if maxNum == num3:
        nextPlane = runway3.pop()
    
    return nextPlane

# printQueue() loops through items and prints the data, formatted
# input:  a queue
# output: a string of plane names and passenger counts
def printQueue(planeQueue, outFile):
    for plane in planeQueue:
        # Write formatted data to file results.txt
        outFile.write("\n%4s %d\
" % (plane.getFlightName(), plane.getNumOfPassengers()))
        # Write formatted data to screen
        print "\t%4s %d" % (plane.getFlightName(), plane.getNumOfPassengers())

        
def calcTime(planeQueue, outFile):

    # Initialize time & passenger count to zero
    totalTime = 0
    totalPassengers = 0
    
    # waitTimeCounter initialized at 1;
    #  it traces the plane's standing and uses that as a mulitplier
    #  for the wait time (first plane only waits 5 minutes; second, ten etc)
    waitTimeCounter = 1
    for plane in planeQueue:
        # Add time for current plane to total
        totalTime += WAIT_TIME * waitTimeCounter * plane.getNumOfPassengers()
        # Get current plane's passenger count and add to total
        totalPassengers += plane.getNumOfPassengers()
        # Increment multiplier value
        waitTimeCounter += 1

    
    outFile.write("\n\nAverage wait time is %.2f minutes \
per person" % (float(totalTime) / totalPassengers))
    print "\n\tAverage wait time is %.2f minutes \
per person" % (float(totalTime) / totalPassengers)

def main():
    printGreeting()
    # Read files
    print "\nFiles runway1.txt, runway2.txt and runway3.txt will now be read."
    runway1 = makeRunway(FILE_ONE)
    runway2 = makeRunway(FILE_TWO)
    runway3 = makeRunway(FILE_THREE)
    
    planeQueue = makeQueue(runway1, runway2, runway3)

    # Open and close outFile as "w" to ensure a blank document
    outFile = open("results.txt", "w")
    outFile.close()

    # Open file to append data
    outFile = open("results.txt", "a")

    # Print results to screen
    print "\nHere are the results (which can be found in results.txt)"
    print
    printQueue(planeQueue, outFile)

    # Call calcTime to determine wait time per passenger
    calcTime(planeQueue, outFile)

    outFile.close()
main()
