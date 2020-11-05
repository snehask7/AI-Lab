#8 queens problem using genetic algorithm
import random
from time import time

class Node:
    def __init__(self, state, fitness):
        self.state = state
        self.fitness = fitness

def fitness_function(node):
    fitness_val = 0
    global n
    # need to find number of attacking pairs
    for i in range(n):
        for j in range(i+1, n):
            if node.state[i] == node.state[j]:
                fitness_val += 1
            elif(abs(i-j) == abs(node.state[i]-node.state[j])):
                fitness_val += 1
    return fitness_val


def random_state():
    board = [-1 for i in range(n)]
    for x in range(8):  # for each column
        board[x] = random.sample(range(0, n), 1)[0]  # random row generated
    return board

def reproduce(node1,node2):
    x=random.sample(range(0, n), 1)[0]  #random crossover pouint
    child1=node1.state[:x]+node2.state[x:]
    child2=node2.state[:x]+node1.state[x:]
    child_node1=Node(child1,-1)
    child_node2=Node(child2,-1)
    child_node1.fitness=fitness_function(child_node1)
    child_node2.fitness=fitness_function(child_node2)
    return child_node1,child_node2

def genetic_algo(population):
    count=0
    while population[0].fitness!=0 :    #fitness value is 0 for the goal state since 0 attacking pairs
        new_population=[]
        for i in range(0,len(population),2):
            x=population[i]
            y=population[i+1]
            child1,child2=reproduce(x,y)    #generating the new states from 2 parent states
            new_population.append(child1)
            new_population.append(child2)
        for x in new_population:    #Mutation
            if(random.random()<0.5):
                x.state[random.sample(range(0, n), 1)[0]]=random.sample(range(0, n), 1)[0]
        population=new_population
        population.sort(key=lambda x: x.fitness)    #sorting by fitness value
        count+=1
    return population[0].state

n = 8
start = Node([6, 7, 2, 4, 7, 5, 8, 8], 0)
population = []
#generating 10 random initial states
k=10
for i in range(10):
    for j in range(k):
        new_state=random_state()
        new_node=Node(new_state,-1)
        new_fitness=fitness_function(new_node)
        new_node.fitness=new_fitness
        population.append(new_node)
    #sorting the initial states by fitness function
    population.sort(key=lambda x: x.fitness)
    before = time()
    print('\nSolution: ',genetic_algo(population))
    print('k is: ',k,' time: ',time()-before)
    if k==10:
        k=100
    else:
        k+=100

"""
Solution:  [2, 5, 1, 6, 0, 3, 7, 4]
k is:  10  time:  5.159706354141235

Solution:  [1, 4, 6, 0, 2, 7, 5, 3]
k is:  100  time:  0.2323436737060547

Solution:  [4, 1, 3, 5, 7, 2, 0, 6]
k is:  200  time:  2.7103233337402344

Solution:  [5, 3, 1, 7, 3, 6, 0, 2]
k is:  300  time:  1.154703140258789

Solution:  [2, 5, 7, 0, 4, 6, 1, 2]
k is:  400  time:  0.30216479301452637

Solution:  [3, 0, 4, 7, 1, 6, 2, 5]
k is:  500  time:  6.342255592346191

Solution:  [5, 1, 6, 0, 2, 4, 7, 2]
k is:  600  time:  4.309746265411377

Solution:  [7, 3, 0, 2, 5, 1, 6, 4]
k is:  700  time:  2.9383857250213623

Solution:  [5, 0, 4, 1, 7, 2, 6, 3]
k is:  800  time:  2.2664549350738525

Solution:  [3, 6, 4, 1, 5, 0, 2, 7]
k is:  900  time:  0.797760009765625
"""