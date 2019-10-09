from openList import openList
import grid_generator
import hValue_gen

counter = 1
deltah = {} #the running sum of all corrections up to the beginning of the xth A* search
pathcost = {}
grid = None

def make_path(current):
    path = []
    while (current.parent is not None and current not in path):
        path.append(current)
        current = current.parent
    path.reverse()
    return path

def initializeState(s, sgoal):
	global deltah
	global pathcost
	global grid
	if (s.search != counter and s.search != 0):
		if (s.gValue + s.hValue < pathcost[str(s.search)]):
			s.hValue = pathcost[str(s.search)] - s.gValue
		s.hValue = s.hValue - (deltah[str(s.counter)] - deltah[str(s.search)])
		s.hValue = max(s.hValue, hValue_gen.hValue(grid, s, sgoal))
		s.gValue = 9999
	elif (s.search == 0):
		s.gValue = 9999
		s.hValue = hValue_gen.hValue(grid, s, sgoal)
	s.search = counter
	grid[s.x][s.y] = s

def computePath(open_list, sgoal):
	global deltah
	global pathcost
	global grid
	while not open_list.isEmpty() and sgoal.gValue > open_list.stateList[1].gValue + open_list.stateList[1].hValue:
		s = open_list.pop()
		neighbors = grid_generator.generate_neighbors([s.x, s.y])
		neighbors = [grid[n[0]][n[1]] for n in neighbors]
		for n in neighbors:
			if (n.gValue > s.gValue + 1):
				n.gValue = s.gValue + 1
				n.parent = s
				if n in open_list.stateList:
					open_list.stateList.remove(n)
				n.fValue = n.hValue + n.gValue
				open_list.addToOpenList(n)
	return open_list

def main(start, goal, the_grid):
	global grid
	global deltah
	global pathcost
	grid = the_grid
	paths = {}
	counter = 1
	deltah[str(counter)] = 0
	sstart = start
	sgoal = goal
	while (sstart != sgoal):
		initializeState(sstart, goal)
		initializeState(sgoal, goal)
		sstart.gValue = 0
		sstart.fValue = sstart.hValue
		open_list = openList(sstart)

		open_list = computePath(open_list, sgoal)

		if open_list.isEmpty():
			pathcost[str(counter)] = 9999
		else:
			pathcost[str(counter)] = sgoal.gValue
			paths[str(counter)] = make_path(sstart)

		sstart = start
		snewgoal = goal

		if sgoal != snewgoal:
			initializeState(snewgoal, goal)
			if snewgoal.gValue + snewgoal.hValue < pathcost[str(counter)]:
				snewgoal.hValue = pathcost[str(counter)] - snewgoal.gValue
				deltah[str(counter + 1)] = deltah[str(counter)] + snewgoal.hValue
				sgoal = snewgoal
		else:
			deltah[str(counter + 1)] = deltah[str(counter)]

		counter += 1
	return min(paths)
