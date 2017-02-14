from NodeTOH import *
from problems.Towers import *

def BiDirectional(problem):
    # For efficiency, we check if the node is a goal state BEFORE putting on the Q
    problem2 = Towers(problem.numDisk, problem.goal)
    # Start the frontier Q by adding the root
    nodeI1 = NodeTOH(problem.initial, [])
    frontierI = deque()
    frontierI.append(nodeI1)

    nodeG1 = NodeTOH(problem2.initial, [])
    frontierG = deque()
    frontierG.append(nodeG1)

    # Keep searching the tree until there is nothing left to explore (i.e. frontier is empty)
    # OR a solution is found

    while len(frontierI) > 0 and len(frontierG) > 0:

        newfrontierG = deque()
        newfrontierGCOPY = deque()

        for i in range(0, len(frontierG)):
            newfrontierG.append(frontierG[i])

        for i in range(0, len(frontierG)):
            newfrontierGCOPY.append(frontierG[i])

        nodeI = frontierI.popleft()
        nodeG = frontierG.popleft()

        childrenI = nodeI.expand(problem)
        childrenG = nodeG.expand(problem2)

        newQueue = deque()

        for childI in childrenI:
            if (childI == []):
                continue
            if(childI.getState()[0] == [] and childI.getState()[1] == []):
                break
            frontierI.append(childI)

        for childG in childrenG:
            if (childG == []):
                continue
            if(childG.getState()[1] == [] and childG.getState()[2] == []):
                    break
            newQueue.append(childG)

        while(newQueue):
            frontierG.append(newQueue.pop())

        for c1 in childrenI:
            if(c1 == []):
                continue
            counter = 0
            while counter < len(newfrontierG):
                element = newfrontierG[counter]
                counter += 1
                if (element != []):
                    if(c1.state == element.getState()):
                        new_list = []
                        for i in range(len(element.actionList) - 1, -1, -1):
                            new_list.append(element.actionList[i])
                        return list(c1.actionList) + new_list

        for c1 in childrenI:
            for c2 in childrenG:
                if(c1 != [] and c2 !=  []):
                    if c1.state == c2.state:
                        new_list = []
                        for i in range(len(c2.actionList) - 1, -1, -1):
                            new_list.append(c2.actionList[i])
                        return list(c1.actionList) + new_list
    return None