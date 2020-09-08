"""
Register Number: 185001157
Name: Sneha Sriram Kannan

DECANTATION PROBLEM

STATE
We can use a 3 element tuple to represent the state.
The state is (a,b,c) : where a represents the 8-litre, b represents the 5-litre jar and c represents the 3-litre jar

Actions: Transfer from 8 litre to 5 litre, 5 litre to 8 litre, 5 litre to 3 litre, 3 litre to 5 litre,  8 litre to 3 litre, 3 litre to 8 litre
INITIAL STATE: (8,0,0)

GOAL STATE(S): (4,1,3), (4,4,0)
"""

#Data structure to store each state and it's parent
class Node:
  def __init__(self, state,parent):
    self.state = state
    self.parent = parent

actions=[[0,1],[1,0],[0,2],[2,0],[1,2],[2,1]]
maxCapacity=[8,5,3]

def printStatesActions(goal):
    print('\nPATH:')
    path=[]
    while goal!=None:
        path.append(goal.state)
        goal=goal.parent
    path.reverse()
    for x in range(len(path)-1):
        print(path[x],end=' ---> ')
    x+=1
    print(path[x])  


#returns the list of neighbors of a given state
def next_states(cs):
    neighbors=[]
    currentState=cs.state
    for x in actions:      
        fromJar=x[0]    #contains 0 or 1 or 2
        toJar=x[1]  #contains 0 or 1 or 2
        newState=currentState[:]
        remainingCapacity=maxCapacity[toJar]-currentState[toJar]
        if(currentState[fromJar]>=remainingCapacity):#can empty contents of from jar into to jar such that from jar becomes empty
            newState[fromJar]=currentState[fromJar]-remainingCapacity
            newState[toJar]=maxCapacity[toJar]
        else:#can fill the to jar but from jar is still not empty
            newState[toJar]=currentState[toJar]+currentState[fromJar]   
            newState[fromJar]=0     
        if(newState!=currentState):
            newNode=Node(newState,cs)
            neighbors.append(newNode)
    return neighbors

#Returns true if the node is a goal state
def isGoalState(node):
    if 4 in node.state:
        return True
    return False

def BFS(initial):    
    frontier=[]
    failure=Node([-1,-1,-1],[-1,-1,-1])
    explored=set()
    frontier.append(initial)
    print('TRACING CONTENTS OF THE QUEUE:')
    while len(frontier)!=0:
        print('QUEUE: ',end="")
        for x in frontier:
            print(x.state,end="")
        print()
        node=frontier.pop(0)
        explored.add(node)
        if(isGoalState(node)): 
            print('\nTHE EXPLORED STATES ARE: ')
            for x in explored:
                print(x.state)
            return node
        for neighbor in next_states(node):   
            #checking if neighbor is in frontier or explored
            found=0
            for f in frontier:
                if(neighbor.state==f.state):
                    found=1
                    break
            if found==0:
                for e in explored:
                    if(e.state==neighbor.state):
                        found=1
            if found==0:
                frontier.append(neighbor)    
    return failure

initialNode=Node([8,0,0],None)
goal=BFS(initialNode)
print('\nINITIAL STATE: ',initialNode.state)
print('\nGOAL STATE: ',goal.state)
printStatesActions(goal)

"""
OUTPUT

TRACING CONTENTS OF THE QUEUE:
QUEUE: [8, 0, 0]
QUEUE: [3, 5, 0][5, 0, 3]
QUEUE: [5, 0, 3][0, 5, 3][3, 2, 3]
QUEUE: [0, 5, 3][3, 2, 3][5, 3, 0]
QUEUE: [3, 2, 3][5, 3, 0]
QUEUE: [5, 3, 0][6, 2, 0]
QUEUE: [6, 2, 0][2, 3, 3]
QUEUE: [2, 3, 3][6, 0, 2]
QUEUE: [6, 0, 2][2, 5, 1]
QUEUE: [2, 5, 1][1, 5, 2]
QUEUE: [1, 5, 2][7, 0, 1]
QUEUE: [7, 0, 1][1, 4, 3]
QUEUE: [1, 4, 3][7, 1, 0]

THE EXPLORED STATES ARE: 
[8, 0, 0]
[3, 2, 3]
[1, 4, 3]
[2, 3, 3]
[3, 5, 0]
[2, 5, 1]
[5, 0, 3]
[5, 3, 0]
[6, 0, 2]
[1, 5, 2]
[7, 0, 1]
[0, 5, 3]
[6, 2, 0]

INITIAL STATE:  [8, 0, 0]

GOAL STATE:  [1, 4, 3]

PATH:
[8, 0, 0] ---> [3, 5, 0] ---> [3, 2, 3] ---> [6, 2, 0] ---> [6, 0, 2] ---> [1, 5, 2] ---> [1, 4, 3]
"""