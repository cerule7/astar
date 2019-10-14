import openList
import hValue_gen
import grid_generator
import state
import forwardastar
import backwardastar
import adaptiveastar

def forwardAStar(start, goal, grid):
	# print('start is {} {}'.format(start.x, start.y))
	# print('goal is {} {}'.format(goal.x, goal.y))

	truePath = []
	agentPosition = start
	start.set_gValue(0)
	start.set_fValue(start.get_hValue())
	start.setStart()
	start.isStart = True
	blockedList = []
	expanded = 1
	while (not agentPosition.isGoal):

		blockedList, result, expanded = forwardastar.traverse_grid(agentPosition, blockedList, grid, expanded)

		if(result == "failed"):
			return ["failed", expanded] 

		#print([(s.x, s.y) for s in blockedList])
		#print([(s.x, s.y) for s in result])
		#print([(s.x, s.y) for s in truePath])

		for position in result:
			if(position.isBlock):
				#print('{} {} is blocked'.format(position.x, position.y))
				blockedList.append(position)
				#agentPosition = position.parent
				#print('{} {} is new agent position'.format(agentPosition.x, agentPosition.y))
				break
			agentPosition = position
			truePath.append(position)
		#print(vars(agentPosition))

	return [truePath, expanded]

def backwardAStar(start, goal, grid):
	#print('start is {} {}'.format(start.x, start.y))
	#print('goal is {} {}'.format(goal.x, goal.y))

	truePath = []
	agentPosition = start
	grid = hValue_gen.generate_hValue(grid, agentPosition.x, agentPosition.y)
	goal.set_gValue(0)
	goal.set_fValue(goal.get_hValue())
	goal.isGoal = True
	start.isStart = True
	blockedList = []
	expanded = 1
	while (not agentPosition.isGoal):

		if(agentPosition.x == goal.x and agentPosition.y + 1 == goal.y):
			truePath.append(grid[agentPosition.x][agentPosition.y + 1])
			break
		if(agentPosition.x + 1 == goal.x and agentPosition.y == goal.y):
			truePath.append(grid[agentPosition.x + 1][agentPosition.y])
			break
		if(agentPosition.x - 1 == goal.x and agentPosition.y == goal.y):
			truePath.append(grid[agentPosition.x - 1][agentPosition.y])
			break
		if(agentPosition.x == goal.x and agentPosition.y == goal.y):
			break

		grid = hValue_gen.generate_hValue(grid, agentPosition.x, agentPosition.y)
		blockedList, result, expanded = backwardastar.traverse_grid(goal, agentPosition, blockedList, grid, expanded)

		if(result == "failed"):
			return ["failed", expanded]

		# print([(s.x, s.y) for s in blockedList])
		# print([(s.x, s.y) for s in result])
		# print([(s.x, s.y) for s in truePath])

		for position in result:
			if(position.isBlock):
				# print('{} {} is blocked'.format(position.x, position.y))
				blockedList.append(position)
				# agentPosition = position.parent
				break
			agentPosition = position
			#print('{} {} is new agent position'.format(agentPosition.x, agentPosition.y))
			truePath.append(position)
		# print(vars(agentPosition))

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
	while (not agentPosition.isGoal):

		blockedList, result, closedList, expanded = adaptiveastar.traverse_grid(agentPosition, blockedList, grid, expanded)

		if(result == "failed"):
			return ["failed", expanded]

		for s in closedList:
			if(s not in blockedList):
				grid[s.x][s.y].hValue = len(result) - s.gValue

		for position in result:
			if(position.isBlock):
				#print('{} {} is blocked'.format(position.x, position.y))
				blockedList.append(position)
				#agentPosition = position.parent
				#print('{} {} is new agent position'.format(agentPosition.x, agentPosition.y))
				break
			agentPosition = position
			truePath.append(position)
		#print(vars(agentPosition))

	return [truePath, expanded]
