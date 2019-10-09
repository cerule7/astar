import numpy
import random
import pickle
import os.path
import state

LENGTH = 20
num_grids = 50
grid_list = []

#this sets isPath and parent to False for the whole grid
def reset(grid):
    for i in grid:
        for j in i:
            j.isPath = False
            j.parent = None
    return grid

def generate_neighbors(cell):
  neighbors = []
  if(cell[0] - 1 >= 0):
    neighbors.append([cell[0] - 1, cell[1]])
  if(cell[0] + 1 < LENGTH):
    neighbors.append([cell[0] + 1, cell[1]])
  if(cell[1] - 1 >= 0):
    neighbors.append([cell[0], cell[1] - 1])
  if(cell[1] + 1 < LENGTH):
    neighbors.append([cell[0], cell[1] + 1])
  return neighbors

def generate_grid():
  global grid_list
  grid = [[state.State(i, j) for i in range(LENGTH)] for j in range(LENGTH)]
  visited = []
  stack = []
  current_cell = [random.randint(0, LENGTH - 1), random.randint(0, LENGTH - 1)]

  while(len(visited) != (LENGTH ** 2)):
    #mark current cell as visited
    if(current_cell not in visited):
      visited.append(current_cell)
    
    #generate neighbors of current cell
    neighbors = generate_neighbors(current_cell)
    neighbors = [n for n in neighbors if n not in visited]

    # if multiple neighbors choose randomly, else choose 1st one, else backtrack, else go to a random cell
    if(len(neighbors) > 1):
      next_cell = neighbors[random.randint(0, len(neighbors) - 1)]
      if(random.randint(0, 9) > 2):
        stack.append(current_cell)
      else:
        grid[current_cell[0]][current_cell[1]].setBlocked()
    elif(len(neighbors) == 1):
      next_cell = neighbors[0]
      if(random.randint(0, 9) > 2):
        stack.append(current_cell)
      else:
        grid[current_cell[0]][current_cell[1]].setBlocked()
    elif(len(stack) != 0):
      next_cell = stack.pop()
    else:
      next_cell = [random.randint(0, LENGTH - 1), random.randint(0, LENGTH - 1)]
      if(next_cell in visited and len(visited) != (LENGTH ** 2)):
        while(next_cell in visited):
          next_cell = [random.randint(0, LENGTH - 1), random.randint(0, LENGTH - 1)]
      if(random.randint(0, 9) > 2):
        stack.append(current_cell)
      else:
        grid[current_cell[0]][current_cell[1]].setBlocked()

    current_cell = [next_cell[0], next_cell[1]]
    if(len(visited) % 1000 == 0):
      print('STEP # ' + str(len(visited)))

  return grid

def grid_in_list(grid, grid_list):
    return next((True for elem in grid_list if numpy.array_equal(elem, grid)), False)

def generate_grid_list():
  global grid_list
  global num_grids
  while(len(grid_list) < num_grids):
    print('GRID # ' + str(len(grid_list)))
    grid = generate_grid()
    if(not grid_in_list(grid, grid_list)):
      grid_list.append(grid)

def save_grid_list():
  global grid_list
  output_file = open('grids', 'wb')
  pickle.dump(grid_list, output_file)
  output_file.close()

def load_grid_list():
  global grid_list
  if(os.path.isfile('grids')):
    gridfile = open('grids', 'rb')
    grid_list = pickle.load(gridfile)
    gridfile.close()

def get_grid_list():
  global grid_list
  return grid_list

def get_random_grid():
  global grid_list
  return grid_list[random.randint(0, len(grid_list) - 1)]
