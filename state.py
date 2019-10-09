class State:
    def __init__(self, a, b):
        self.x = b
        self.y = a
        self.parent = None
        self.gValue = 9999
        self.hValue = 0
        self.fValue = 9999 #g + h
        self.isGoal = False
        self.isBlock = False
        self.isPath = False
        self.isStart = False
        self.isOccupied = False
        self.search = 0

    def getParent(self):
        return self.parent

    def getX(self):
        return self.x

    def getY(self):
        return self.y

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

    def setStart(self):
        self.isStart = True

    def setGoal(self):
        self.isGoal = True

    def setPath(self):
        self.isPath = True
    def set_parent(self, par):
        self.parent = par

    def toString(self):
        if(self.isBlock):
            return 'X'
        elif(self.isGoal):
            return 'G'
        elif(self.isStart):
            return 'S'
        elif(self.isPath):
            return '*'
        else:
            return '_'
