import hValue_gen
import forwardastar
import backwardastar
import adaptiveastar
import grid_generator

def printPath(grid, path):
	for s in path:
		if (not grid[s.x][s.y].isGoal and not grid[s.x][s.y].isStart):
			grid[s.x][s.y].isPath = True
	print("")
	print('initial path: ')
	for g in grid:
		for k in g:
			print(k.toString(), end = " ")
		print("")
	print("")
	print("")
	grid = grid_generator.reset(grid)

def forwardAStar(start, tiebreaker, goal, grid):
	truePath = []
	agentPosition = start
	start.set_gValue(0)
	start.set_fValue(start.get_hValue())
	start.setStart()
	start.isStart = True
	blockedList = []
	expanded = 1
	count = 0
	while (not agentPosition.isGoal):

		blockedList, result, expanded = forwardastar.traverse_grid(agentPosition, tiebreaker, blockedList, grid, expanded)

		if(result == "failed"):
			return ["failed", expanded]

		if count == 0:
			printPath(grid, result)
			count = 1

		for position in result:
			if(position.isBlock):
				blockedList.append(position)
				break
			agentPosition = position
			truePath.append(position)
	return [truePath, expanded]


def backwardAStar(start, goal, grid):
	truePath = []
	agentPosition = start
	goal.set_gValue(0)
	goal.set_fValue(goal.get_hValue())
	goal.isGoal = True
	start.isStart = True
	blockedList = []
	expanded = 1
	grid = hValue_gen.generate_hValue(grid, start.x, start.y)
	count = 0
	while (not agentPosition.isGoal):
		if(agentPosition.x == goal.x and agentPosition.y+1 == goal.y):
			truePath.append(grid[agentPosition.x] [agentPosition.y+1])
			break
		if (agentPosition.x+1 == goal.x and agentPosition.y == goal.y):
			truePath.append(grid[agentPosition.x+1][agentPosition.y])
			break
		if(agentPosition.x == goal.x and agentPosition.y == goal.y): break
		grid = hValue_gen.generate_hValue(grid, agentPosition.x, agentPosition.y)
		blockedList, result, expanded = backwardastar.traverse_grid(goal, blockedList, grid, expanded, agentPosition.x, agentPosition.y)

		if(result == "failed"):
			return ["failed", expanded]

		if count == 0:
			printPath(grid, result)
			count = 1

		for position in result:
			if(position.isBlock):
				blockedList.append(position)
				break
			agentPosition = position

			truePath.append(position)
	return [truePath, expanded]


def adaptiveAStar(start, goal, grid):
	truePath = []
	agentPosition = start
	start.set_gValue(0)
	start.set_fValue(start.get_hValue())
	start.setStart()
	start.isStart = True
	blockedList = []
	expanded = 1
	count = 0 
	while (not agentPosition.isGoal):

		blockedList, result, closedList, expanded = adaptiveastar.traverse_grid(agentPosition, blockedList, grid, expanded)

		if(result == "failed"):
			return ["failed", expanded]

		if count == 0:
			printPath(grid, result)
			count = 1

		for s in closedList:
			grid[s.x][s.y].hValue = len(result) - s.gValue

		for position in result:
			if(position.isBlock):
				blockedList.append(position)
				break
			agentPosition = position
			truePath.append(position)
	return [truePath, expanded]