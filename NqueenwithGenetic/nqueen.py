from AIproblem import *
from algorithms.geneticAlgorithmsM import *
import random

class nqueen(AIproblem):
    def __init__(self, initialState,size, goal=None):
        AIproblem.__init__(self,initialState,size,evalFn=None, goal=None)
        self.initial = initialState 
        self.size = size #size of board
        self.population = None
        self.evalFn = self.evaluation
        self.parents = []
        self.child = NQueensProblemState([],self.size)


    # self.initial could be something like NQueenState object
    # self.initial.state could be something like [0,1,2,...]

    def population_generator(self):
        population = []
        k = self.size*5
        for i in range(k):
            newstate1 = NQueensProblemState([random.randrange(0,self.size) for x in range(0,self.size)],self.size)
            newstate1.evaluate(self.evalFn)
            population.append(newstate1)
        self.population = population
        for i in range(len(population)):
            print('each board represent',population[i].state)
        return self.population
    
    def getRandomAction( self, state ):
        return None

    def getActions( self, state ) :
        # state could be something like NQueenState object
        # state.state could be something like [0,1,2,...]
        # produce a list of actions to be applied to the current state
        # Pruning could happen here (i.e. only generate legal actions that result in legal states)
        return []

    def applyAction ( self, state, action ) :
        # Does nothing but copy the current state. This will be problem specific.
        # Apply the action to the current state to produce a new state
        # If you did not check for illegal states in getActions, then check for illegal states here
        # Can evaluate node based on path cost, heuristic function, or fitness function
        if not action :
            return []
        else :
            newState = deepcopy(state)
            return newState

    def evaluation( self, state):
        counter = 0
        diagonal_conflict = 0
        horizontal_conflict = 0
        for row in range(len(state)):
            for col in range(len(state)):
                if row != col:
                    if (row - state[row] == col - state[col]) or (row + state[row] == col + state[col]):
                        diagonal_conflict += 1
                    if state[row] == state[col]:
                        horizontal_conflict += 1
        fitness = horizontal_conflict + diagonal_conflict
        return fitness

    def randomSelection(self):
        probabilityofeach = [self.population[i].value for i in range(len(self.population))]
        for i in range(len(self.population)):
            print(probabilityofeach[i]) 
        smallestindex = heapq.nsmallest(2,probabilityofeach)
        print('smallestindex is:',smallestindex)
        parent1 = self.population[(probabilityofeach.index(smallestindex[0]))]
        parent2 = self.population[(probabilityofeach.index(smallestindex[1]))]
        print('self.parents are:,', parent1.state,parent2.state)
        self.parents = (parent1,parent2)

    def reproduce(self):
        n = self.parents[0].size
        parent1 = self.parents[0]
        parent2 = self.parents[1]
        c = int(random.randrange(n))
        child1 = []
        child2 = []
        for i in range(0,c+1):
            child1.append(parent1.state[i])
        for i in range(c+1, n):
            child2.append(parent2.state[i])
        b = child1+child2
        self.child.state = b
        self.child.evaluate(self.evalFn)
        print('self.child.state is:',self.child.state)
        return self.child

    def mutate(self):
        n = len(self.child.state)
        index = int(random.randrange(n))
        changeto = int(random.randrange(n))
        self.child.state[index] = changeto
        self.child.evaluate(self.evalFn)
        print('self.child.state is:',self.child.state)
        return self.child

    def isGoal ( self, state ):
        if (state.value == 0):
            return True
        # Determine if current state is goal
        return False

class NQueensProblemState(ProblemState):
    def __init__( self, state, size ):
        ProblemState.__init__(self, state,size, value=0)
	# self.state = [0,1,2,3..]
	# self.size = n size of the board
    def evaluate( self, evalFn ):
        self.value = evalFn( self.state)
    def isGoal( self ) :
        return False
	# Some problems have rules that determine the goal state (e.g. Sudoku), while other problems
	# have a known goal state (e.g. Sliding Puzzle).
	# It might be appropriate to leave goal checking to this State class, or it might be better to
	# have it checked in the Problem State.
    def __str__( self ) :
        # Converts the state representation to a string (nice for printing)
        return str( self.state )

