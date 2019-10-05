import state
import os.path
import grid_generator
import hValue_gen
import random
import forwardastar
import backwardastar

if (os.path.isfile('grids')):
    grid_generator.load_grid_list()
else:
    grid_generator.generate_grid_list()
    grid_generator.save_grid_list()

grid = grid_generator.get_random_grid()

i = random.randint(0, len(grid) - 1)# goal x
j = random.randint(0, len(grid) - 1)# goal y

grid[i][j].setGoal()
grid[i][j].isBlock = False

x = random.randint(0, len(grid) - 1)# start x
y = random.randint(0, len(grid) - 1)# start y

# check start does not equal goal:
while x == i:
    x = random.randint(0, len(grid) - 1)

grid[x][y].setStart()
grid[x][y].isBlock = False

grid = hValue_gen.generate_hValue(grid, i, j)

print('forward a star found: ')

result = forwardastar.traverse_grid(state.State(y, x, 0), grid)

if (result == 'failed'):
    print('no path to goal found')
else:
    for s in result:
        if (not grid[s.x][s.y].isGoal and not grid[s.x][s.y].isStart):
            grid[s.x][s.y].isPath = True

for g in grid:
    for k in g:
        print(k.toString(), end = " ")
    print("")

print('backward a star found: ')

grid = grid_generator.reset(grid)
result = backwardastar.traverse_grid(state.State(j, i, 0), grid)

if (result == 'failed'):
    print('no path to goal found')
else:
    for s in result:
        if (not grid[s.x][s.y].isGoal and not grid[s.x][s.y].isStart):
            grid[s.x][s.y].isPath = True

for g in grid:
    for k in g:
        print(k.toString(), end = " ")
    print("")

