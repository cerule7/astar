import numpy
import random 

def generate_neighbors(cell):
  neighbors = []
  if(cell[0] - 1 >= 0):
    neighbors.append([cell[0] - 1, cell[1]])
  if(cell[0] + 1 < 101):
    neighbors.append([cell[0] + 1, cell[1]])
  if(cell[1] - 1 >= 0):
    neighbors.append([cell[0], cell[1] - 1])
  if(cell[1] + 1 < 101):
    neighbors.append([cell[0], cell[1] + 1])
  return neighbors

def generate_grid():
  grid = numpy.zeros((101, 101))
  visited = []
  stack = []
  current_cell = [random.randint(0, 100), random.randint(0, 100)]

  while(len(visited) != 10201):
    #mark current cell as visited
    if(current_cell not in visited):
      visited.append(current_cell)
    
    neighbors = generate_neighbors(current_cell)
    neighbors = [n for n in neighbors if n not in visited]

    if(len(neighbors) > 1):
      next_cell = neighbors[random.randint(0, len(neighbors) - 1)]
      if(random.randint(0, 9) > 2):
        stack.append(current_cell)
      else:
        grid[current_cell[0], current_cell[1]] = 1
    elif(len(neighbors) == 1):
      next_cell = neighbors[0]
      if(random.randint(0, 9) > 2):
        stack.append(current_cell)
      else:
        grid[current_cell[0], current_cell[1]] = 1
    elif(len(stack) != 0):
      next_cell = stack.pop()
    else:
      next_cell = [random.randint(0, 100), random.randint(0, 100)]
      if(next_cell in visited and len(visited) != 10201):
        while(next_cell in visited):
          next_cell = [random.randint(0, 100), random.randint(0, 100)]
      if(random.randint(0, 9) > 2):
        stack.append(current_cell)
      else:
        grid[current_cell[0], current_cell[1]] = 1

    current_cell = [next_cell[0], next_cell[1]]
    if(len(visited) % 1000 == 0):
      print('STEP # ' + str(len(visited)))

  return grid

def grid_in_list(grid, grid_list):
    return next((True for elem in grid_list if numpy.array_equal(elem, grid)), False)

grid_list = []

while(len(grid_list) < 50):
  print('GRID # ' + str(len(grid_list)))
  grid = generate_grid()
  if(not grid_in_list(grid, grid_list)):
    grid_list.append(grid)

for g in grid_list:
  print(g)



