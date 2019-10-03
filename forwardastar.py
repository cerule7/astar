from openList import openList
import grid_generator

def make_path(cameFrom, current):
	print(['{}: {}'.format((k.x, k.y), (cameFrom[k].x, cameFrom[k].y)) for k in cameFrom.keys()])
	path = [current]
	while current in cameFrom:
		current = cameFrom[current]
		path.append(current)
	path.reverse()
	return path

def traverse_grid(start_state, grid):
	open_list = openList(start_state)
	closed_list = []

	start_state.set_gValue(0)
	start_state.set_fValue(start_state.get_hValue)
	cameFrom = {}
	while(not open_list.isEmpty()):

		# get lowest f score node from open list
		current = open_list.pop()
		closed_list.append(current)

		print('current is {} {}'.format(current.x, current.y))
		# grid[current.y][current.x].setPath()
		# for g in grid:
		# 	for i in g:
		# 		print(i.toString(), end=" ")
		# 	print("")

		# if it's the goal, return path to goal
		if(current.isGoal):
			return make_path(cameFrom, current)

		neighbors = grid_generator.generate_neighbors([current.x, current.y])
		neighbors = [grid[n[0]][n[1]] for n in neighbors]
		for n in neighbors:
			if(n in closed_list):
				continue

			if(n.isBlock):
				closed_list.append(n)
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
