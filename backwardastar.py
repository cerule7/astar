from openList import openList
import grid_generator

def make_path(current):
    path = []
    while current.getParent():
        current.isPath = True
        path.append(current)
        current = current.parent
    return path

def traverse_grid(goal_state, grid):
    open_list = openList(goal_state)
    closed_list = []

    goal_state.set_gValue(0)
    goal_state.set_fValue(goal_state.get_hValue)
    while(not open_list.isEmpty()):
        # get lowest f score node from open list
        current = open_list.pop()
        closed_list.append(current)

        # if it's the start, return path to start
        if(current.isStart):
            return make_path(current)

        neighbors = grid_generator.generate_neighbors([current.x, current.y])
        neighbors = [grid[n[0]][n[1]] for n in neighbors]
        for n in neighbors:
            if(n in closed_list):
                continue
            if(n.isBlock):
                closed_list.append(n)
                continue

            # distance from one node to another is 1
            new_gScore = current.get_gValue() + 1

            if(n in open_list.stateList):
                if n.get_gValue() > new_gScore:
                    n.set_gValue(new_gScore)
                    n.parent = current 
            elif new_gScore < n.get_gValue():
                n.parent = current
                n.set_gValue(new_gScore)
                n.set_fValue(n.get_gValue() + n.get_hValue())
                open_list.addToOpenList(n)

    return "failed"