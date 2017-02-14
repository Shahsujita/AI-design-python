import random
import heapq
        
def population_generator(n,k):
    population = []
    for i in range(k):
        population.append([random.randrange(0,n) for x in range(0,n)])
    return population

def fitness_fn(individual):
    counter = 0
    diagonal_conflict = 0
    horizontal_conflict = 0
    for row in range(len(individual)):
        for col in range(len(individual)):
            if row != col:
                if (row - individual[row] == col - individual[col]) or (row + individual[row] == col + individual[col]):
                    diagonal_conflict += 1
                if individual[row] == individual[col]:
                    horizontal_conflict += 1
    fitness = horizontal_conflict + diagonal_conflict
    return fitness

def randomSelection(population,fitness_fn):
    probabilityofeach = []
    overallfitness = []
    currentfitness = 0
    totalfitness = sum([fitness_fn(x) for x in population])
    for i in range(len(population)):
        count = fitness_fn(population[i])/totalfitness
        probabilityofeach.append(count)
        currentfitness += count
        overallfitness.append(currentfitness)
    smallestindex = heapq.nsmallest(2,probabilityofeach)
    parent1 = population[(probabilityofeach.index(smallestindex[0]))]
    parent2 = population[(probabilityofeach.index(smallestindex[1]))]
    return (parent1,parent2)
    
            
def reproduce(parent1, parent2):
    n = len(parent1)
    c = int(random.randrange(n))
    child1 = []
    child2 = []
    for i in range(0,c+1):
        child1.append(parent1[i])
    for i in range(c+1, n):
        child2.append(parent2[i])
    b = child1+child2
    return b

def mutate(child):
    n = len(child)
    index = int(random.randrange(n))
    changeto = int(random.randrange(n))
    child[index] = changeto
    return child
    
        
def genetic_algorithm(testcase):
    print('calling genetic_algorithm')
    n = testcase
    k = n*5
    population = population_generator(n,k)
    maxgeneration = 5000
    n = maxgeneration
    while n> 0:
        new_population = []
        for i in range(len(population)):
            parents = []
            parents = randomSelection(population, fitness_fn)
            child = reproduce(parents[0],parents[1])
            if random.uniform(0,1) < 1.0:
                child = mutate(child)
            new_population.append(child)
            if fitness_fn(child) == 0:
                return child
            parents = []
        population = new_population
        n -= 1
    print('failed')
    return None

