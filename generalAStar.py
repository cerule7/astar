import openList
import hValue_gen
import grid_generator
import state
import forwardastar
import backwardastar

def astar(start, goal, grid):
	print('start is {} {}'.format(start.x, start.y))
	print('goal is {} {}'.format(goal.x, goal.y))

	truePath = []
	agentPosition = start
	start.set_gValue(0)
	start.set_fValue(start.get_hValue())
	start.setStart()
	start.isStart = True
	blockedList = []
	while (not agentPosition.isGoal):

		blockedList, result = forwardastar.traverse_grid(agentPosition, blockedList, grid)

		if(result == "failed"):
			return "failed"

		print([(s.x, s.y) for s in blockedList])
		print([(s.x, s.y) for s in result])
		print([(s.x, s.y) for s in truePath])

		for position in result:
			if(position.isBlock):
				print('{} {} is blocked'.format(position.x, position.y))
				blockedList.append(position)
				#agentPosition = position.parent
				print('{} {} is new agent position'.format(agentPosition.x, agentPosition.y))
				break
			agentPosition = position
			truePath.append(position)
		print(vars(agentPosition))

	return truePath

