import state
import os.path
import grid_generator
import hValue_gen
import generalAStar
import statistics 

LENGTH = 101

def runAlgorithm(type, grid):

    if(type == 'backward'):
        [result, expanded] = generalAStar.backwardAStar(state.State(0, 0), state.State(LENGTH - 1, LENGTH - 1), grid)
    elif(type == 'forward'):
        [result, expanded] = generalAStar.forwardAStar(state.State(0, 0), state.State(LENGTH - 1, LENGTH - 1), grid)
    else:
        [result, expanded] = generalAStar.adaptiveAStar(state.State(0, 0), state.State(LENGTH - 1, LENGTH - 1), grid)

    return [result, expanded]

if (os.path.isfile('grids')):
    grid_generator.load_grid_list()
else:
    grid_generator.generate_grid_list()
    grid_generator.save_grid_list()

#statistic section
gridlist = grid_generator.get_grid_list()
expansions = list()

i = 1
for grid in gridlist:
    grid[LENGTH - 1][LENGTH - 1].setGoal()
    grid[LENGTH - 1][LENGTH - 1].isBlock = False

    grid[0][0].setStart()
    grid[0][0].isBlock = False

    grid = hValue_gen.generate_hValue(grid, LENGTH - 1, LENGTH - 1)

    [result, expanded] = runAlgorithm('backward', grid)
    print('grid #{} expanded {}'.format(i, expanded))
    expansions.append(expanded)
    i += 1

print('statistics on backward expansions for 50 grids: ')
print('mean: {}'.format(statistics.mean(expansions)))
print('median: {}'.format(statistics.median(expansions)))
print('standard dev: {}'.format(statistics.stdev(expansions)))
print('maximum: {}'.format(max(expansions)))
print('minimum: {}'.format(min(expansions)))
