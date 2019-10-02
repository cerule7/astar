import openList
import grid_generator

def make_path(cameFrom, current):
	path = [current]
	while current in cameFrom.keys:
		current = cameFrom[current]
		path.insert(0, current)
	return path

def traverse_grid(start_state, grid):
	open_list = openList(start_state)
	closed_list = []

	start_state.set_hValue(0)
	start_state.set_fValue(start_state.get_hValue)
	cameFrom = {}

	while(not open_list.isEmpty()):

		# get lowest f score node from open list
		current = open_list.pop()
		closed_list.append(current)

		# if it's the goal, return path to goal
		if(current.isGoal()):
			return make_path(cameFrom, current)

		neighbors = grid_generator.generate_neighbors(current)
		for n in neighbors:
			if(n in closed_list):
				continue
			# distance from one node to another is 1
			new_gScore = current.get_gValue() + 1
			# if current node
			if new_gScore < n.get_gValue():
				cameFrom[n] = current
				n.set_gValue = new_gScore
				n.set_fValue = n.get_gValue() + n.get_hValue()
				open_list.addToOpenList(n)

	return "failed"
