#8 puzzle problem using DFS
from copy import deepcopy
from collections import deque
class Node:
  def __init__(self, state,parent):
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
    neighbors=[]
    currentState=cs.state       
    newState=deepcopy(currentState)
    x_pos=0
    y_pos=0
    for i in range(3):
        for j in range(3):
            if currentState[i][j]==0:
                x_pos=i
                y_pos=j
                break
    #moving blank space left
    if y_pos!=0:
        newState[x_pos][y_pos]=newState[x_pos][y_pos-1]
        newState[x_pos][y_pos-1]=0
        newNode=Node(newState,cs)
        neighbors.append(newNode)
    newState=deepcopy(currentState)

    #moving blank space right
    if y_pos!=2:
        newState[x_pos][y_pos]=newState[x_pos][y_pos+1]
        newState[x_pos][y_pos+1]=0
        newNode=Node(newState,cs)
        neighbors.append(newNode)
    newState=deepcopy(currentState)

    #moving blank space top
    if x_pos!=0:
        newState[x_pos][y_pos]=newState[x_pos-1][y_pos]
        newState[x_pos-1][y_pos]=0
        newNode=Node(newState,cs)
        neighbors.append(newNode)
    newState=deepcopy(currentState)

    #moving blank space bottom
    if x_pos!=2:
        newState[x_pos][y_pos]=newState[x_pos+1][y_pos]
        newState[x_pos+1][y_pos]=0
        newNode=Node(newState,cs)
        neighbors.append(newNode)
    return neighbors

def isGoalState(node):
    goal_state=[[0,1,2],[3,4,5],[6,7,8]]
    if node.state==goal_state:
        return True
    return False

def BFS(initial):    
    frontier=deque([])
    failure=None
    explored=set()
    explored.add(tuple(tuple(j) for j in initial.state))              
    frontier.append(initial)
    if isGoalState(initial):         
        return initial
    while len(frontier)!=0:
        node=frontier.popleft()        
        for neighbor in next_states(node):   
            if(isGoalState(neighbor)):                                 
                return neighbor
            if tuple(tuple(j) for j in neighbor.state) not in explored:  
                explored.add(tuple(tuple(j) for j in neighbor.state))              
                frontier.append(neighbor)    

initial_state=[[7, 2, 4], [0, 5, 6], [8, 3, 1]]    # 0 represents the blank space
initial=Node(initial_state,None)
goal=BFS(initial)
print('GOAL STATE: ',goal.state)
printStatesActions(goal)

"""
OUTPUT

GOAL STATE:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

PATH:
[[7, 2, 4], [0, 5, 6], [8, 3, 1]] ---> [[0, 2, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 0, 4], [7, 5, 6], [8, 3, 1]] ---> [[2, 5, 4], [7, 0, 6], [8, 3, 1]] ---> [[2, 5, 4], [7, 6, 0], [8, 3, 1]] ---> [[2, 5, 4], [7, 6, 1], [8, 3, 0]] ---> [[2, 5, 4], [7, 6, 1], [8, 0, 3]] ---> [[2, 5, 4], [7, 6, 1], [0, 8, 3]] ---> [[2, 5, 4], [0, 6, 1], [7, 8, 3]] ---> [[2, 5, 4], [6, 0, 1], [7, 8, 3]] ---> [[2, 5, 4], [6, 1, 0], [7, 8, 3]] ---> [[2, 5, 4], [6, 1, 3], [7, 8, 0]] ---> [[2, 5, 4], [6, 1, 3], [7, 0, 8]] ---> [[2, 5, 4], [6, 1, 3], [0, 7, 8]] ---> [[2, 5, 4], [0, 1, 3], [6, 7, 8]] ---> [[2, 5, 4], [1, 0, 3], [6, 7, 8]] ---> [[2, 5, 4], [1, 3, 0], [6, 7, 8]] ---> [[2, 5, 0], [1, 3, 4], [6, 7, 8]] ---> [[2, 0, 5], [1, 3, 4], [6, 7, 8]] ---> [[0, 2, 5], [1, 3, 4], [6, 7, 8]] ---> [[1, 2, 5], [0, 3, 4], [6, 7, 8]] ---> [[1, 2, 5], [3, 0, 4], [6, 7, 8]] ---> [[1, 2, 5], [3, 4, 0], [6, 7, 8]] ---> [[1, 2, 0], [3, 4, 5], [6, 7, 8]] ---> [[1, 0, 2], [3, 4, 5], [6, 7, 8]] ---> [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
"""