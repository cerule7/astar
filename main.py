import state
import os.path
import grid_generator

if(os.path.isfile('grids')):
	grid_generator.load_grid_list()
else:
	grid_generator.generate_grid_list()
	grid_generator.save_grid_list()

grid = grid_generator.get_random_grid()
for g in grid:
	for i in g:
		print(i.toString(), end=" ")
	print("")