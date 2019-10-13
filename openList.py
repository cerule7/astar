import state
import math
import random

class openList:
    def __init__(self, states):  # states will be initial starting state.
        s = state.State  # s is a dummy value in first position of list so that open list index may start at 1
        s.fValue = -1
        self.stateList = [s]
        self.stateList.append(states)
        self.bubbleUp(len(self.stateList) - 1)

    def addToOpenList(self, state, tieBreak = None): #tiebreak determines how to break ties, bigG -> prioritize bigger gValues, smallG -> prioritizes small gValues
        self.stateList.append(state)
        if(tieBreak == 'bigG'):
            self.bubbleUpBigG(len(self.stateList) - 1)
        elif(tieBreak == 'smallG'):
            self.bubbleUpSmallG(len(self.stateList) - 1)
        else:
            self.bubbleUp(len(self.stateList) - 1)

    def isEmpty(self):
        if len(self.stateList) <= 1:
            return True
        else:
            return False

    def swap(self, i, j):
        self.stateList[i], self.stateList[j] = self.stateList[j], self.stateList[i]

    def pop(self):
        if len(self.stateList) == 1:
            top = False
        elif len(self.stateList) == 2:
            top = self.stateList.pop()
        else:
            self.swap(1, (len(self.stateList) - 1))
            top = self.stateList.pop()
            self.bubbleDown(1)
        return top

    def bubbleUp(self, i):
        if i <= 1:
            return
        else:
            parent = math.trunc(i / 2)
            if self.stateList[parent].fValue > self.stateList[i].fValue:
                self.swap(parent, i)
                self.bubbleUp(parent)

    def bubbleDown(self, i):
        leftChild = i * 2
        rightChild = (i * 2) + 1
        small = i  # assumed smallest fValue
        if len(self.stateList) > leftChild and self.stateList[leftChild].fValue < self.stateList[small].fValue:
            small = leftChild
        if len(self.stateList) > rightChild and self.stateList[rightChild].fValue < self.stateList[small].fValue:
            small = rightChild
        if small == i:
            return
        else:
            self.swap(i, small)
            self.bubbleDown(small)

    def bubbleUpBigG(self, i): #tie break that prioritizes values with larger g values
        if i <= 1:
            return
        else:
            parent = math.trunc(i / 2)
            if self.stateList[parent].fValue > self.stateList[i].fValue:
                self.swap(parent, i)
                self.bubbleUp(parent)
            elif self.stateList[parent].fValue == self.stateList[i].fValue: #if fValues are equal, must tie break
                if self.stateList[parent].gValue < self.stateList[i].gValue: #if the parent has a smaller g value, then prioritize child and swap
                    self.swap(parent, i)
                    self.bubbleUp(parent)
                else:
                    randomTieBreak = random.randint(0, 1)
                    if(randomTieBreak == 1):
                        self.swap(parent, i)
                        self.bubbleUp(parent)

    def bubbleUpSmallG(self, i):  # tie break that prioritizes values with smaller g values
        if i <= 1:
            return
        else:
            parent = math.trunc(i / 2)
            if self.stateList[parent].fValue > self.stateList[i].fValue:
                self.swap(parent, i)
                self.bubbleUp(parent)
            elif self.stateList[parent].fValue == self.stateList[i].fValue: #if fValues are equal, must tie break
                if self.stateList[parent].gValue > self.stateList[i].gValue: #if the parent has a bigger g value, then prioritize child and swap
                    self.swap(parent, i)
                    self.bubbleUp(parent)
                else:
                    randomTieBreak = random.randint(0, 1)
                    if (randomTieBreak == 1):
                        self.swap(parent, i)
                        self.bubbleUp(parent)
