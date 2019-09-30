class State:
    def __init__(self, counter):
        self.gValue
        self.hValue
        self.fValue = self.gValue + self.hValue
        self.isGoal = False
        self.isBlock = False
        self.isOccupied = False
        self.search = counter

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
    def agentOccupy(self):
        self.isOccupied = True
    def blocked(self):
        self.isBlock = True




