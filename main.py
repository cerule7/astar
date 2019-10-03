import state
import os.path
import grid_generator
import hValue_gen
import random
import forwardastar

if(os.path.isfile('grids')):
	grid_generator.load_grid_list()
else:
	grid_generator.generate_grid_list()
	grid_generator.save_grid_list()

grid = grid_generator.get_random_grid()

i = random.randint(0, len(grid) - 1) #goal x
j = random.randint(0, len(grid) - 1) #goal y

grid[i][j].setGoal()
grid[i][j].isBlock = False

x = random.randint(0, len(grid) - 1) #start x
y = random.randint(0, len(grid) - 1) #start y

grid[x][y].setStart()
grid[x][y].isBlock = False

grid = hValue_gen.generate_hValue(grid, i, j)

for g in grid:
	for i in g:
		print(i.toString(), end=" ")
	print("")

print('forward a star')
result = forwardastar.traverse_grid(state.State(x, y, 0), grid)
print(result)
