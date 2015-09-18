#!/usr/bin/python 

## Emily Stohl
## 9/18/2015
## Homework #3 (Programming Assignment 2)

import sys 

# Command line input:
FileName = sys.argv[1] # should be World1.txt or World2.txt
HeuristicNum = sys.argv[2] # should be 1 or 2

# Select function to be used for calculating heuristic
if HeuristicNum == '1':
	from heuristic_1 import *
elif HeuristicNum == '2':
	from heuristic_2 import *
else:
	print("Invalid heuristic number")
	
# Import world to be searched
File = open(FileName, 'r')
matrix = []
for line in File:
	thisrow = []
	for num in line:
		if num == '0' or num == '1' or num == '2':
			thisrow.append(num)
	if len(thisrow) != 0 :
		matrix.append(thisrow)		
File.close()
# world will be saved as an array using lists 

rows = len(matrix) # number of rows in world
cols = len(matrix[0]) # number of columns in world

# End Node is located at (0, cols-1), used to calculate heuristic values
EndRow = 0
EndCol = cols - 1


# Node class to be used in search
class Node:
	def __init__(self, row_loc, col_loc, Value):
		self.row = row_loc # row number 
		self.col = col_loc # col number
		self.val = Value # '0' = open or '1' = mountain or '2' = wall
		self.parent = None # parent node 
		self.f = 10000 # cost: distToStart + heuristic value
		self.h = heuristic(row_loc, col_loc, EndRow, EndCol) # heuristic value
		self.distToStart = 0 
		if Value == '2':
			self.closed = 2
		else:
			self.closed = 0 # 0 if not in Open and unvisited, 1 if in Open, 2 if it has been visited or if wall
		
# Create array of nodes to be used in search
NodeArray = []
for i in range(0, rows):
	thisrow = []
	for j in range(0, cols):
		thisrow.append(Node(i, j, matrix[i][j]))
	NodeArray.append(thisrow)
	
	
	
	
	
	
# A* Search:	

def Cost(Value, Diag): # Returns cost to travel to the square
	if (Value == '0') and (Diag == False):
		return 10
	if (Value == '0') and (Diag == True):
		return 14
	if (Value == '1') and (Diag == False):
		return 20
	if (Value == '1') and (Diag == True):
		return 24
	if Value == '2':
		return 1000 # Will not matter because square will never be visited



# Start Node is the bottom left corner: NodeArray[rows-1][0]
# End Node is the top right corner: NodeArray[0][cols-1]

NodeArray[rows-1][0].f = 0 + NodeArray[rows-1][0].h
Open = [[rows-1, 0]] # open is a list of (row, col) points, initialized with Start
NodeArray[rows-1][0].closed = 1

SquaresExplored = 0 # Count of how many squares are visited before the end is found


while len(Open) > 0:
	
	# Find node with lowest cost
	MinCost = 10000
	for i in range(0, len(Open)):
		if NodeArray[Open[i][0]][Open[i][1]].f < MinCost:
			MeRow = Open[i][0]
			MeCol = Open[i][1]
			MinCost = NodeArray[MeRow][MeCol].f

	Open.remove([MeRow, MeCol])
	NodeArray[MeRow][MeCol].closed = 2
	SquaresExplored = SquaresExplored + 1
	
	
	# Search adjacent squares

	# North square:
	if 0 < MeRow:  
		Diag = False
		Value = NodeArray[MeRow-1][MeCol].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow-1][MeCol].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow-1][MeCol].distToStart: # shorter distance by this path
				NodeArray[MeRow-1][MeCol].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow-1][MeCol].distToStart = Dist
				NodeArray[MeRow-1][MeCol].f = Dist + NodeArray[MeRow-1][MeCol].h		
		if NodeArray[MeRow-1][MeCol].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow-1][MeCol].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow-1][MeCol].distToStart = Dist
			NodeArray[MeRow-1][MeCol].f = Dist + NodeArray[MeRow-1][MeCol].h
			Open.append([MeRow-1, MeCol])
			NodeArray[MeRow-1][MeCol].closed = 1
			
	# North East square:	
	if (0 < MeRow) and (MeCol < cols-1):		
		Diag = True
		Value = NodeArray[MeRow-1][MeCol+1].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow-1][MeCol+1].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow-1][MeCol+1].distToStart: # shorter distance by this path
				NodeArray[MeRow-1][MeCol+1].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow-1][MeCol+1].distToStart = Dist
				NodeArray[MeRow-1][MeCol+1].f = Dist + NodeArray[MeRow-1][MeCol+1].h		
		if NodeArray[MeRow-1][MeCol+1].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow-1][MeCol+1].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow-1][MeCol+1].distToStart = Dist
			NodeArray[MeRow-1][MeCol+1].f = Dist + NodeArray[MeRow-1][MeCol+1].h
			Open.append([MeRow-1, MeCol+1])
			NodeArray[MeRow-1][MeCol+1].closed = 1
			
	# East square:	
	if MeCol < cols-1:		
		Diag = False
		Value = NodeArray[MeRow][MeCol+1].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow][MeCol+1].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow][MeCol+1].distToStart: # shorter distance by this path
				NodeArray[MeRow][MeCol+1].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow][MeCol+1].distToStart = Dist
				NodeArray[MeRow][MeCol+1].f = Dist + NodeArray[MeRow][MeCol+1].h		
		if NodeArray[MeRow][MeCol+1].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow][MeCol+1].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow][MeCol+1].distToStart = Dist
			NodeArray[MeRow][MeCol+1].f = Dist + NodeArray[MeRow][MeCol+1].h
			Open.append([MeRow, MeCol+1])
			NodeArray[MeRow][MeCol+1].closed = 1
			
			
	# South East square:	
	if (MeCol < cols-1) and (MeRow < rows - 1): 
		Diag = True
		Value = NodeArray[MeRow+1][MeCol+1].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow+1][MeCol+1].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow+1][MeCol+1].distToStart: # shorter distance by this path
				NodeArray[MeRow+1][MeCol+1].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow+1][MeCol+1].distToStart = Dist
				NodeArray[MeRow+1][MeCol+1].f = Dist + NodeArray[MeRow+1][MeCol+1].h		
		if NodeArray[MeRow+1][MeCol+1].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow+1][MeCol+1].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow+1][MeCol+1].distToStart = Dist
			NodeArray[MeRow+1][MeCol+1].f = Dist + NodeArray[MeRow+1][MeCol+1].h
			Open.append([MeRow+1, MeCol+1])
			NodeArray[MeRow+1][MeCol+1].closed = 1

	# South square:		
	if MeRow < rows - 1: 
		Diag = False
		Value = NodeArray[MeRow+1][MeCol].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow+1][MeCol].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow+1][MeCol].distToStart: # shorter distance by this path
				NodeArray[MeRow+1][MeCol].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow+1][MeCol].distToStart = Dist
				NodeArray[MeRow+1][MeCol].f = Dist + NodeArray[MeRow+1][MeCol].h		
		if NodeArray[MeRow+1][MeCol].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow+1][MeCol].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow+1][MeCol].distToStart = Dist
			NodeArray[MeRow+1][MeCol].f = Dist + NodeArray[MeRow+1][MeCol].h
			Open.append([MeRow+1, MeCol])
			NodeArray[MeRow+1][MeCol].closed = 1
			
	# South West square:		
	if (MeRow < rows - 1) and (0 < MeCol):
		Diag = True
		Value = NodeArray[MeRow+1][MeCol-1].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow+1][MeCol-1].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow+1][MeCol-1].distToStart: # shorter distance by this path
				NodeArray[MeRow+1][MeCol-1].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow+1][MeCol-1].distToStart = Dist
				NodeArray[MeRow+1][MeCol-1].f = Dist + NodeArray[MeRow+1][MeCol-1].h		
		if NodeArray[MeRow+1][MeCol-1].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow+1][MeCol-1].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow+1][MeCol-1].distToStart = Dist
			NodeArray[MeRow+1][MeCol-1].f = Dist + NodeArray[MeRow+1][MeCol-1].h
			Open.append([MeRow+1, MeCol-1])
			NodeArray[MeRow+1][MeCol-1].closed = 1

	# West square:
	if 0 < MeCol:  
		Diag = False
		Value = NodeArray[MeRow][MeCol-1].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow][MeCol-1].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow][MeCol-1].distToStart: # shorter distance by this path
				NodeArray[MeRow][MeCol-1].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow][MeCol-1].distToStart = Dist
				NodeArray[MeRow][MeCol-1].f = Dist + NodeArray[MeRow][MeCol-1].h		
		if NodeArray[MeRow][MeCol-1].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow][MeCol-1].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow][MeCol-1].distToStart = Dist
			NodeArray[MeRow][MeCol-1].f = Dist + NodeArray[MeRow][MeCol-1].h
			Open.append([MeRow, MeCol-1])
			NodeArray[MeRow][MeCol-1].closed = 1
			
	# North West square:
	if (0 < MeCol)  and (0 < MeCol):
		Diag = True
		Value = NodeArray[MeRow-1][MeCol-1].val
		Dist = NodeArray[MeRow][MeCol].distToStart + Cost(Value, Diag)
		if NodeArray[MeRow-1][MeCol-1].closed == 1: # square was placed in Open by another path
			if Dist < NodeArray[MeRow-1][MeCol-1].distToStart: # shorter distance by this path
				NodeArray[MeRow-1][MeCol-1].parent = NodeArray[MeRow][MeCol]
				NodeArray[MeRow-1][MeCol-1].distToStart = Dist
				NodeArray[MeRow-1][MeCol-1].f = Dist + NodeArray[MeRow-1][MeCol-1].h		
		if NodeArray[MeRow-1][MeCol-1].closed == 0: #square has not been visited or placed in open
			NodeArray[MeRow-1][MeCol-1].parent = NodeArray[MeRow][MeCol]
			NodeArray[MeRow-1][MeCol-1].distToStart = Dist
			NodeArray[MeRow-1][MeCol-1].f = Dist + NodeArray[MeRow-1][MeCol-1].h
			Open.append([MeRow-1, MeCol-1])
			NodeArray[MeRow-1][MeCol-1].closed = 1

		
	# Check if end has been found
	if Open.count([EndRow, EndCol]) == 1:
		Open = [] # will exit out of while loop 


# Record results of found path
Order = []
Next = NodeArray[EndRow][EndCol]
while Next != NodeArray[rows-1][0]:
	Order.append([Next.row, Next.col])
	Next = Next.parent
Order.append([Next.row, Next.col]) # Append Start Node
Order.reverse()

# Required output of results
print('\nPath Traveled (listed as [row, column]):')
print(Order)
print('Distance cost: ' +  str(NodeArray[EndRow][EndCol].distToStart))
print('Locations Evaluated: ' + str(SquaresExplored))	
print('')
		
		
