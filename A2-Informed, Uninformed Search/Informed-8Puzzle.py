# 8 puzzle problem using DFS
from copy import deepcopy
from collections import deque
import heapdict 

class Node:
  def __init__(self, state, parent):
    self.state = state
    self.parent = parent

def printStatesActions(goal):
    path = []
    while goal != None:
        path.append(goal.state)
        goal = goal.parent
    print('\nLENGTH OF THE PATH: ',len(path),'\n')
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
    man_dist=0
    for i in range(3):
        for j in range(3):
            x=node.state[i][j]//3
            y=node.state[i][j]%3
            man_dist+=abs(x-i)+abs(y-j)        
    return man_dist


def GreedyBFS(initial):
    frontier = heapdict.heapdict() 
    failure = None
    explored = set()
    # explored.add(tuple(tuple(j) for j in initial.state))
    frontier[initial]=heuristic(initial)
    while len(frontier) != 0:
        node=frontier.popitem()[0]    
        if(isGoalState(node)):
            return node
        explored.add(tuple(tuple(j) for j in node.state))    
        for neighbor in next_states(node):   
            if tuple(tuple(j) for j in neighbor.state) not in explored and neighbor not in frontier.keys():  
                frontier[neighbor]=heuristic(neighbor)   
    return failure   



initial_state=[[7, 2, 4], [ 5,0, 6], [8, 3, 1]]    # 0 represents the blank space
initial=Node(initial_state,None)
goal=GreedyBFS(initial)
if(goal!=None):
    print('GOAL STATE: ',goal.state)
    printStatesActions(goal)

