from openList import openList
import grid_generator

def make_path(current):
    path = []
    while (current.parent is not None and current not in path):
        path.append(current)
        current = current.parent
    path.reverse()
    return path

def traverse_grid(goal_state, blockList, grid):
    open_list = openList(goal_state)
    closed_list = []

    goal_state.set_fValue(goal_state.get_hValue())

    neighbors = grid_generator.generate_neighbors([goal_state.x, goal_state.y])
    neighbors = [grid[n[0]][n[1]] for n in neighbors]

    for n in neighbors:
        if n in blockList:
            continue
        if (n.isBlock):
            n.set_gValue(9999)
            n.set_fValue(n.get_hValue()+n.get_gValue())
            blockList.append(n)
        else:
            n.set_gValue(1)
            n.set_fValue(n.get_hValue() + n.get_gValue())
            open_list.addToOpenList(n)
            n.parent = goal_state

    while (not open_list.isEmpty()):
        # get lowest f score node from open list
        current = open_list.pop()
        closed_list.append(current)
        # if it's the goal, return path to goal
        if (current.isStart):
            return [blockList, make_path(current)]

        neighbors = grid_generator.generate_neighbors([current.x, current.y])
        neighbors = [grid[n[0]][n[1]] for n in neighbors]
        for n in neighbors:
            if (n in closed_list or n in blockList):
                continue

            # distance from one node to another is 1
            new_gScore = current.get_gValue() + 1

            if (n in open_list.stateList):
                if n.get_gValue() > new_gScore:
                    n.set_gValue(new_gScore)
                    n.set_fValue(n.get_gValue() + n.get_hValue())
                    n.parent = current
            elif (new_gScore < n.get_gValue() or n not in open_list.stateList):
                n.parent = current
                n.set_gValue(new_gScore)
                n.set_fValue(n.get_gValue() + n.get_hValue())
                open_list.addToOpenList(n)

    return [blockList, "failed"]