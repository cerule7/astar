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

i = random.randint(0, 10) #goal x
j = random.randint(0, 10) #goal y

grid[i][j].setGoal()

grid = hValue_gen.generate_hValue(grid, i, j)

for g in grid:
	for i in g:
		print(i.toString(), end=" ")
	print("")

x = random.randint(0, 10) #start x
y = random.randint(0, 10) #start y

grid[x][y].setStart()

print('forward a star')
result = forwardastar.traverse_grid(grid[x][y], grid)
print(result)
