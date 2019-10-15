from openList import openList
import grid_generator


def make_path(current):
    path = []
    while (current.parent is not None and current not in path):
        path.append(current)
        current = current.parent
    return path


def traverse_grid(start_state, blockList, grid, expanded, agentx, agenty):
    open_list = openList(start_state)
    closed_list = []

    start_state.set_fValue(start_state.get_hValue())

    neighbors = grid_generator.generate_neighbors([start_state.x, start_state.y])
    neighbors = [grid[n[0]][n[1]] for n in neighbors]

    for n in neighbors:
        if(n.x == 100 and n.y == 100):
            n.parent = start_state
            return [blockList, make_path(n), expanded]
        if n in blockList:
            continue
        if (n.isBlock):
            n.set_gValue(9999)
            n.set_fValue(n.get_hValue() + n.get_gValue())
            blockList.append(n)
        else:
            n.set_gValue(1)
            n.set_fValue(n.get_hValue() + n.get_gValue())
            open_list.addToOpenList(n, 'bigG')
            n.parent = start_state

    while (not open_list.isEmpty()):
        # get lowest f score node from open list
        current = open_list.pop('bigG')
        closed_list.append(current)
        expanded += 1

        # if it's the goal, return path to goal
        if (current.x == agentx and current.y == agenty):
            return [blockList, make_path(current), expanded]

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
                open_list.addToOpenList(n, 'bigG')
    return [blockList, "failed", expanded]