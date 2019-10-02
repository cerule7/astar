class State:
    def __init__(self, counter):
        self.gValue = float("inf")
        self.hValue = 0
        self.fValue = float("inf") #g + h
        self.isGoal = False
        self.isBlock = False
        self.isOccupied = False
        self.search = counter

    def set_gValue(self, g):
        self.gValue = g

    def set_hValue(self, h):
        self.hValue = h

    def set_fValue(self, f):
        self.fValue = f

    def get_gValue(self):
        return self.gValue

    def get_hValue(self):
        return self.hValue

    def get_fValue(self):
        return self.fValue

    def makeGoal(self):
        self.isGoal = True
        self.gValue = 0
        self.hValue = 0
        self.fValue = 0

    def setOccupied(self):
        self.isOccupied = True

    def setBlocked(self):
        self.isBlock = True

    def toString(self):
        if(self.isBlock):
            return 'X'
        else:
            return '_'



