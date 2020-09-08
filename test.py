import heapdict
h = heapdict.heapdict() 
  
class Node:
  def __init__(self, state, parent,path_cost):
    self.state = state
    self.parent = parent
    self.path_cost=path_cost

initial_state=[[7, 2, 4], [0, 5, 6], [8, 3, 1]]    # 0 represents the blank space
initial=Node(initial_state,None,0)

h[initial]= 0

for x in h.items():
    print(x[0].state)