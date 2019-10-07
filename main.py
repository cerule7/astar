import state
import os.path
import grid_generator
import hValue_gen
import random
import forwardastar
import backwardastar
import generalAStar

LENGTH = 50

if (os.path.isfile('grids')):
    grid_generator.load_grid_list()
else:
    grid_generator.generate_grid_list()
    grid_generator.save_grid_list()

grid = grid_generator.get_random_grid()

#i = random.randint(0, len(grid) - 1)# goal x
#j = random.randint(0, len(grid) - 1)# goal y

grid[LENGTH - 1][LENGTH - 1].setGoal()
grid[LENGTH - 1][LENGTH - 1].isBlock = False

#x = random.randint(0, len(grid) - 1)# start x
#y = random.randint(0, len(grid) - 1)# start y

# check start does not equal goal:
#while x == i:
#    x = random.randint(0, len(grid) - 1)

grid[0][0].setStart()
grid[0][0].isBlock = False

grid = hValue_gen.generate_hValue(grid, LENGTH - 1, LENGTH - 1)

print('backwardastar a star found: ')

result = generalAStar.backwardAStar(state.State(0, 0, 0), state.State(LENGTH - 1, LENGTH - 1, 0), grid)

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
