#Assuming a 10x10 matrix

def manhattan(center,points):
    dist=0
    for p in points:
        dist+=abs(p[0]-center[0])+abs(p[1]-center[1])
    return dist

def next_states(point):
    npt=[]
    if(point[0]+1<10):
        npt.append((point[0]+1,point[1]))
    if(point[0]-1>=0):
        npt.append((point[0]-1,point[1]))
    if(point[1]+1<9):
        npt.append((point[0],point[1]+1))
    if(point[1]-1>=0):
        npt.append((point[0]+1,point[1]-1))
    return npt

def next_center(center,points):
	while True:
		next = next_states(center)
		dist = [ manhattan(next_pt, points) for next_pt in next ]
		min_dist = min(dist)
		ind = dist.index(min_dist)
		if manhattan(center, points) > min_dist:
			center = next[ind]
		else:
			break        
	return center


points=[]
n=int(input("enter number of points:"))
for i in range(1,n+1):
    print("Point ",i," :")
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    points.append((x,y))
print("Center of points ",points,"is : ",next_center((7,0),points))


