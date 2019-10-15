import state
import os.path
import grid_generator
import hValue_gen
import generalAStar
import random

LENGTH = 101

def runAlgorithm(type, grid):

    if(type == 'backward'):
        [result, expanded] = generalAStar.backwardAStar(state.State(0, 0), state.State(LENGTH - 1, LENGTH - 1), grid)
    elif(type == 'forward-big'):
        [result, expanded] = generalAStar.forwardAStar(state.State(0, 0), 'bigG', state.State(LENGTH - 1, LENGTH - 1), grid)
    elif(type == 'forward-small'):
        [result, expanded] = generalAStar.forwardAStar(state.State(0, 0), 'smallG', state.State(LENGTH - 1, LENGTH - 1), grid)
    else:
        [result, expanded] = generalAStar.adaptiveAStar(state.State(0, 0), state.State(LENGTH - 1, LENGTH - 1), grid)

    return [result, expanded]

#load grid
if (os.path.isfile('grids')):
    grid_generator.load_grid_list()
else:
    grid_generator.generate_grid_list()
    grid_generator.save_grid_list()


gridlist = grid_generator.get_grid_list()
expansions = list()

grid = gridlist[random.randint(0, 49)]

grid[LENGTH - 1][LENGTH - 1].setGoal()
grid[LENGTH - 1][LENGTH - 1].isBlock = False

grid[0][0].setStart()
grid[0][0].isBlock = False

print('initial grid')

for g in grid:
    for k in g:
        print(k.toString(), end = " ")
    print("")

for algorithm in ['forward-big', 'forward-small', 'backward', 'adaptive']:
    print(algorithm + "'s results: ")
    grid = hValue_gen.generate_hValue(grid, LENGTH - 1, LENGTH - 1)

    [result, expanded] = runAlgorithm(algorithm, grid)
    print('number of nodes expanded: {}'.format(expanded))

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

    grid = grid_generator.reset(grid)


