from time import time
# 8 puzzle problem using DFS
from copy import deepcopy
from collections import deque
import heapdict
import heapq


class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.path_cost = None

    def __lt__(self, a):
        return self.state < a.state


def printStatesActions(goal):
    path = []
    while goal != None:
        path.append(goal.state)
        goal = goal.parent
    print('\nLENGTH OF THE PATH: ', len(path), '\n')
    path.reverse()
    print('PATH:\n')
    for x in range(len(path)-1):
        print(path[x], end=' ---> ')
    x += 1
    print(path[x])


def next_states(cs):
    neighbors = []
    currentState = cs.state
    newState = deepcopy(currentState)
    x_pos = 0
    y_pos = 0
    for i in range(3):
        for j in range(3):
            if currentState[i][j] == 0:
                x_pos = i
                y_pos = j
                break
    # moving blank space left
    if y_pos != 0:
        newState[x_pos][y_pos] = newState[x_pos][y_pos-1]
        newState[x_pos][y_pos-1] = 0
        newNode = Node(newState, cs)
        neighbors.append(newNode)
    newState = deepcopy(currentState)

    # moving blank space right
    if y_pos != 2:
        newState[x_pos][y_pos] = newState[x_pos][y_pos+1]
        newState[x_pos][y_pos+1] = 0
        newNode = Node(newState, cs)
        neighbors.append(newNode)
    newState = deepcopy(currentState)

    # moving blank space top
    if x_pos != 0:
        newState[x_pos][y_pos] = newState[x_pos-1][y_pos]
        newState[x_pos-1][y_pos] = 0
        newNode = Node(newState, cs)
        neighbors.append(newNode)
    newState = deepcopy(currentState)

    # moving blank space bottom
    if x_pos != 2:
        newState[x_pos][y_pos] = newState[x_pos+1][y_pos]
        newState[x_pos+1][y_pos] = 0
        newNode = Node(newState, cs)
        neighbors.append(newNode)
    return neighbors


def isGoalState(node):
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    if node.state == goal_state:
        return True
    return False


def heuristic(node):
    man_dist = 0
    for i in range(3):
        for j in range(3):
            x = node.state[i][j]//3
            y = node.state[i][j] % 3
            man_dist += abs(x-i)+abs(y-j)
    return man_dist


def BFS(initial):
    frontier = deque([])
    failure = None
    explored = set()
    explored.add(tuple(tuple(j) for j in initial.state))
    frontier.append(initial)
    if isGoalState(initial):
        return initial
    while len(frontier) != 0:
        node = frontier.popleft()
        for neighbor in next_states(node):
            if(isGoalState(neighbor)):
                return neighbor
            if tuple(tuple(j) for j in neighbor.state) not in explored:
                explored.add(tuple(tuple(j) for j in neighbor.state))
                frontier.append(neighbor)


def GreedyBFS(initial):
    frontier = []
    failure = None
    explored = set()
    heapq.heappush(frontier, (heuristic(initial), initial))
    while len(frontier) != 0:
        node = heapq.heappop(frontier)[1]
        if(isGoalState(node)):
            return node
        explored.add(tuple(tuple(j) for j in node.state))
        for neighbor in next_states(node):
            found = 0
            for x in frontier:
                if x[1].state == neighbor.state:
                    found = 1
            if tuple(tuple(j) for j in neighbor.state) not in explored and found == 0:
                heapq.heappush(frontier, (heuristic(neighbor), neighbor))
    return failure


def AStar(initial):
    frontier = heapdict.heapdict()
    failure = None
    explored = set()
    frontier[initial] = heuristic(initial)
    while len(frontier) != 0:
        node = frontier.popitem()[0]
        if(isGoalState(node)):
            return node
        explored.add(tuple(tuple(j) for j in node.state))
        for neighbor in next_states(node):
            neighbor.path_cost = node.path_cost+1
            new_cost = heuristic(neighbor)+neighbor.path_cost
            if tuple(tuple(j) for j in neighbor.state) not in explored and neighbor not in frontier.keys():
                frontier[neighbor] = new_cost
            elif neighbor in frontier.keys() and frontier[neighbor] > new_cost:
                frontier[neighbor] = new_cost
    return failure


# 0 represents the blank space
initial_state = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
initial = Node(initial_state, None)
initial.path_cost = 0
print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('BFS\n')
before = time()
goal = BFS(initial)
if(goal != None):
    print('GOAL STATE: ', goal.state)
    print('\nTIME: ', time()-before)
    printStatesActions(goal)
print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('Greedy BFS\n')
before = time()
goal = GreedyBFS(initial)
if(goal != None):
    print('GOAL STATE: ', goal.state)
    print('\nTIME: ', time()-before)
    printStatesActions(goal)
print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('A* Search\n')
before = time()
goal = AStar(initial)
if(goal != None):
    print('GOAL STATE: ', goal.state)
    print('\nTIME: ', time()-before)
    printStatesActions(goal)

"""

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BFS

GOAL STATE:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

TIME:  13.357528686523438

LENGTH OF THE PATH:  27 

PATH:

[[7, 2, 4], [5, 0, 6], [8, 3, 1]] ---> [[7, 2, 4], [0, 5, 6], [8, 3, 1]] ---> [[0, 2, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 0, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 5, 4], [7, 0, 6], [8, 3, 1]] ---> [[2, 5, 4], [7, 6, 0], [8, 3, 1]] ---> [[2, 5, 4], [7, 6, 1], [8, 3, 0]] ---> [[2, 5, 4], [7, 6, 1], [8, 0, 3]] ---> [[2, 5, 4], [7, 6, 1], [0, 8, 3]] ---> [[2, 5, 4], [0, 6, 1], [7, 8, 3]] ---> [[2, 5, 4], [6, 0, 1], [7, 8, 3]] ---> [[2, 5, 4], [6, 1, 0], [7, 8, 3]] ---> [[2, 5, 4], [6, 1, 3], [7, 8, 0]] ---> [[2, 5, 4], [6, 1, 3], [7, 0, 8]] ---> [[2, 5, 4], [6, 1, 3], [0, 7, 8]] ---> [[2, 5, 4], [0, 1, 3], [6, 7, 8]] ---> [[2, 5, 4], [1, 0, 3], [6, 7, 8]] ---> [[2, 5, 4], [1, 3, 0], [6, 7, 8]] ---> [[2, 5, 0], [1, 3, 4], [6, 7, 8]] ---> [[2, 0, 5], [1, 3, 4], [6, 7, 8]] ---> [[0, 2, 5], [1, 3, 4], [6, 7, 8]] ---> [[1, 2, 5], [0, 3, 4], [6, 7, 8]] ---> [[1, 2, 5], [3, 0, 4], [6, 7, 8]] ---> [[1, 2, 5], [3, 4, 0], [6, 7, 8]] ---> [[1, 2, 0], [3, 4, 5], [6, 7, 8]] ---> [[1, 0, 2], [3, 4, 5], [6, 7, 8]] ---> [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Greedy BFS

GOAL STATE:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

TIME:  0.011887073516845703

LENGTH OF THE PATH:  31 

PATH:

[[7, 2, 4], [5, 0, 6], [8, 3, 1]] ---> [[7, 2, 4], [0, 5, 6], [8, 3, 1]] ---> [[0, 2, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 0, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 4, 0], [7, 5, 6], [8, 3, 1]] ---> [[2, 4, 6], [7, 5, 0], [8, 3, 1]] ---> [[2, 4, 6], [7, 0, 5], [8, 3, 1]] ---> [[2, 4, 6], [7, 3, 5], [8, 0, 1]] ---> [[2, 4, 6], [7, 3, 5], [0, 8, 1]] ---> [[2, 4, 6], [0, 3, 5], [7, 8, 1]] ---> [[2, 4, 6], [3, 0, 5], [7, 8, 1]] ---> [[2, 0, 6], [3, 4, 5], [7, 8, 1]] ---> [[2, 6, 0], [3, 4, 5], [7, 8, 1]] ---> [[2, 6, 5], [3, 4, 0], [7, 8, 1]] ---> [[2, 6, 5], [3, 0, 4], [7, 8, 1]] ---> [[2, 0, 5], [3, 6, 4], [7, 8, 1]] ---> [[0, 2, 5], [3, 6, 4], [7, 8, 1]] ---> [[3, 2, 5], [0, 6, 4], [7, 8, 1]] ---> [[3, 2, 5], [6, 0, 4], [7, 8, 1]] ---> [[3, 2, 5], [6, 4, 0], [7, 8, 1]] ---> [[3, 2, 5], [6, 4, 1], [7, 8, 0]] ---> [[3, 2, 5], [6, 4, 1], [7, 0, 8]] ---> [[3, 2, 5], [6, 4, 1], [0, 7, 8]] ---> [[3, 2, 5], [0, 4, 1], [6, 7, 8]] ---> [[3, 2, 5], [4, 0, 1], [6, 7, 8]] ---> [[3, 2, 5], [4, 1, 0], [6, 7, 8]] ---> [[3, 2, 0], [4, 1, 5], [6, 7, 8]] ---> [[3, 0, 2], [4, 1, 5], [6, 7, 8]] ---> [[3, 1, 2], [4, 0, 5], [6, 7, 8]] ---> [[3, 1, 2], [0, 4, 5], [6, 7, 8]] ---> [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
A* Search

GOAL STATE:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

TIME:  0.4018595218658447

LENGTH OF THE PATH:  27 

PATH:

[[7, 2, 4], [5, 0, 6], [8, 3, 1]] ---> [[7, 2, 4], [0, 5, 6], [8, 3, 1]] ---> [[0, 2, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 0, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 5, 4], [7, 0, 6], [8, 3, 1]] ---> [[2, 5, 4], [7, 3, 6], [8, 0, 1]] ---> [[2, 5, 4], [7, 3, 6], [0, 8, 1]] ---> [[2, 5, 4], [0, 3, 6], [7, 8, 1]] ---> [[2, 5, 4], [3, 0, 6], [7, 8, 1]] ---> [[2, 5, 4], [3, 6, 0], [7, 8, 1]] ---> [[2, 5, 0], [3, 6, 4], [7, 8, 1]] ---> [[2, 0, 5], [3, 6, 4], [7, 8, 1]] ---> [[0, 2, 5], [3, 6, 4], [7, 8, 1]] ---> [[3, 2, 5], [0, 6, 4], [7, 8, 1]] ---> [[3, 2, 5], [6, 0, 4], [7, 8, 1]] ---> [[3, 2, 5], [6, 4, 0], [7, 8, 1]] ---> [[3, 2, 5], [6, 4, 1], [7, 8, 0]] ---> [[3, 2, 5], [6, 4, 1], [7, 0, 8]] ---> [[3, 2, 5], [6, 4, 1], [0, 7, 8]] ---> [[3, 2, 5], [0, 4, 1], [6, 7, 8]] ---> [[3, 2, 5], [4, 0, 1], [6, 7, 8]] ---> [[3, 2, 5], [4, 1, 0], [6, 7, 8]] ---> [[3, 2, 0], [4, 1, 5], [6, 7, 8]] ---> [[3, 0, 2], [4, 1, 5], [6, 7, 8]] ---> [[3, 1, 2], [4, 0, 5], [6, 7, 8]] ---> [[3, 1, 2], [0, 4, 5], [6, 7, 8]] ---> [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
"""