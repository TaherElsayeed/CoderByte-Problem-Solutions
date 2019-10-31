
from math import sqrt

class ClosestEnemyII:

    def __init__(self, strArr):
        self.startingX = None   # This will hold the x coordinate of 1
        self.startingY = None   # This will hold the y coordinate of 1
        self.twoCoordinates = None
        self.oneCoordinates = None
        self.shortestCoordinates = None

        temp = []
        for x in range(len(strArr)):
            if x == 0:
                pass
            else:
                temp.append(strArr[-x])
        temp.append(strArr[0])

        self.strArr = temp  # This reverses the input list in order for it to be printed easily

# getOneCoordinates, getTwoCoordinates, and hypotenuse are all helper functions for findShortestHypotenuse
    def getOneCoordinates(self):
        for foo in range(len(self.strArr)):
            for bar in range(len(self.strArr[foo])):
                if self.strArr[foo][bar] == "1":
                    self.startingX = bar
                    self.startingY = foo
        self.oneCoordinates = [(self.startingX, self.startingY)]
        return self.oneCoordinates

    def getTwoCoordinates(self):
        temp = []
        for foo in range(len(self.strArr)):
            for bar in range(len(self.strArr[foo])):
                if self.strArr[foo][bar] == "2":
                    temp.append((bar, foo))
        if temp == []:
            quit(0)
        self.twoCoordinates = temp
        return self.twoCoordinates

    def hypotenuse(self, a:int, b:int):
        return sqrt(a ** 2 + b **2)
    
    # findShortestHypotenuse is a helper function for calculate
    def findShortestHypotenuse(self):
        self.getOneCoordinates()
        self.getTwoCoordinates()
        temp = []
        for foo in self.twoCoordinates:
            a = abs(self.oneCoordinates[0][0] - foo[0])
            b = abs(self.oneCoordinates[0][1] - foo[1])
            temp.append((foo, self.hypotenuse(a, b)))
        
        self.shortestCoordinates = [(temp[0][0], temp[0][1])]

        for bar in temp:
            if bar[1] < self.shortestCoordinates[0][1]:
                self.shortestCoordinates = [(bar[0], bar[1])]
        
        return self.shortestCoordinates

    # Calculate is the only function in this class that will output a desired result
    def calculate(self):
        self.findShortestHypotenuse()
        xSteps = abs(self.oneCoordinates[0][0] - self.shortestCoordinates[0][0][0])
        ySteps = abs(self.oneCoordinates[0][1] - self.shortestCoordinates[0][0][1])
        return xSteps + ySteps
