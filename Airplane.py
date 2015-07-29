class Airplane:

        #constructor
        def __init__(self, flightName, numOfPassengers):
                self.flightName = str(flightName)
                self.numOfPassengers = numOfPassengers

        #accessors (one line to save space)
        def getFlightName(self): return self.flightName
        def getNumOfPassengers(self): return int (self.numOfPassengers)

        #mutators
        def setFlightName(self, newFlightName): self.flightName = newFlightName
        def setNumOfPassengers(self, newNumOfPassengers):
                self.numOfPassengers = newNumOfPassengers

        #other methods
        def display(self): return "%5s %5s" % (self.flightName, self.numOfPassengers)

# Airplane literally becomes a data type like int, char, etc.

