import random

class Node:
    def __init__(self, x,y):
        self.x=x
        self.y=y

def gen_random_point(grid_x,grid_y):
    x=random.sample(range(0,grid_x),1)[0]
    y=random.sample(range(0,grid_y),1)[0]
    start=Node(x,y)
    return start

def find_manhattan_distance(current_point):
    cost=0
    for point in points:
        cost+=abs(current_point.x-point.x)+abs(current_point.y-point.y)
    return cost

def hill_climb(start_point):
    actions=[[0,1],[1,0],[0,-1],[-1,0]] #up,right,down,left
    point=start_point
    min_cost=100000
    while True:
        initial_mincost=min_cost
        for movement in actions:
            new_point=Node(point.x+movement[0],point.y+movement[1])
            if new_point.x>=0 and new_point.y>=0:   #within grid
                new_cost=find_manhattan_distance(new_point)
                if new_cost<min_cost:
                    min_cost=new_cost
                    min_point=new_point
        if min_cost>=initial_mincost:
            return min_point
        else:
            point=min_point
        
start_point=gen_random_point(10,9)
print('START POINT: (',start_point.x,',',start_point.y,')')
A=Node(1,7)
B=Node(9,4)
C=Node(4,2)
D=Node(2,3)
E=Node(7,1)
points=[A,B,C,D,E]
center=hill_climb(start_point)
print('CENTER POINT: (',center.x,',',center.y,')')
print('MANHATTAN DISTANCE: ',find_manhattan_distance(center))

"""
OUTPUT

START POINT: ( 7 , 0 )
CENTER POINT: ( 4 , 3 )
MANHATTAN DISTANCE:  21

"""1