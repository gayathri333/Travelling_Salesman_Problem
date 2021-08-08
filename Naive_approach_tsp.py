#Program to implement the naive algorithm for solving the 
#traveling salesman problem 
from sys import maxsize 
from itertools import permutations
import random
import time
start_time = time.time()

#Function to implement the traveling salesman problem 
def travelingSalesmanProb(graph,source): 

	# Storing all vertices apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != source: 
			vertex.append(i) 

	# Storing the minimum weight Hamiltonian Cycle 
	minimumPath = maxsize 
	nextPermutation = permutations(vertex)
	for i in nextPermutation:

		# Storing the current Path weight(cost) 
		currentPathweight = 0

		# Computing the current path weight 
		p = source 
		for j in i: 
			currentPathweight += graph[p][j] 
			p = j 
		currentPathweight += graph[p][source] 

		# Updating minimum 
		minimumPath = min(minimumPath, currentPathweight) 
		
	return minimumPath 


# Driver Code 
if __name__ == "__main__": 

	global V, graph
	graph = []
	V = random.randint(3,10)
	print("The number of cities/vertices: ", V)
	
	print("The entries row-wise: ") # Here, entries can be distance between 2 cities etc
	# For user input 
	for i in range(V):          # for loop for row entries 
		a =[] 
		for j in range(V):      # for loop for column entries 
			val = random.randint(0,1000000)
			a.append(val)
			print(val)
		graph.append(a) 

	source = 0
	print("Minimum path :", travelingSalesmanProb(graph, source)) #Printing the final answer
	print("--- %s seconds ---" % (time.time() - start_time))