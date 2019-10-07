import state
import os.path
import grid_generator
import hValue_gen
import random
import forwardastar
import backwardastar
import generalAStar

LENGTH = 10

def runAlgorithm(type, grid):
    print('{} a star found: '.format(type))

    if(type == 'backward'):
        result = generalAStar.backwardAStar(state.State(0, 0, 0), state.State(LENGTH - 1, LENGTH - 1, 0), grid)
    elif(type == 'forward'):
        result = generalAStar.forwardAStar(state.State(0, 0, 0), state.State(LENGTH - 1, LENGTH - 1, 0), grid)

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

if (os.path.isfile('grids')):
    grid_generator.load_grid_list()
else:
    grid_generator.generate_grid_list()
    grid_generator.save_grid_list()

grid = grid_generator.get_random_grid()

grid[LENGTH - 1][LENGTH - 1].setGoal()
grid[LENGTH - 1][LENGTH - 1].isBlock = False

grid[0][0].setStart()
grid[0][0].isBlock = False

grid = hValue_gen.generate_hValue(grid, LENGTH - 1, LENGTH - 1)

runAlgorithm('forward', grid)
runAlgorithm('backward', grid)
