#!/usr/bin/python 

## Emily Stohl
## 10/7/2015
## Homework #5 (Programming Assignment 3)
## Markov Decision Processes

## Note about varying the value of epsilon:
# Changing the value of epsilon did not create a different path or give significantly 
# different utility values. The utility sum was approximately 237 each time. The values 
# of epsilon tested were 0, 0.1, 0.2, ..., 0.8, 0.9, 1.0

import sys 

# Command line input:
FileName = sys.argv[1] 
Epsilon = float(sys.argv[2])

# Import world to be searched
File = open(FileName, 'r')
matrix = []
is50 = False # because 50 is two characters, checks to make sure 5 and 0 is not appended instead of 50

for line in File:
	thisrow = []
	for num in line:
		if num != ' ' and num != '\n':
			if is50 == False:
				thisrow.append(num)
			if is50 == True:
				is50 = False
			if num == '5':
				is50 = True # determines where the 50 (apple) is; won't append the 0 after the 5
	if len(thisrow) != 0 :
		matrix.append(thisrow)		
File.close()
# world will be saved as an array using lists 

rows = len(matrix) # number of rows in world
cols = len(matrix[0]) # number of columns in world


# properties of each state and creating array of the state class:

class State:
	def __init__(self, row_loc, col_loc, Value):
		self.row = row_loc # row number 
		self.col = col_loc # col number
		self.value = Value # 1 if mountain, 2 if wall, 3 if snakes, 4 if barn, 5 if apple, 0 otherwise
		self.utility= 0
		self.visit = False # To be used in the end to find the path
		# reward: 
		if Value == 1: # mountain
			self.reward = -1.0 
		elif Value == 3: # snakes
			self.reward = -2.0
		elif Value == 4: # barn
			self.reward = 5.0
		elif Value == 5: # apple (end state)
			self.reward = 50.0
			self.utility = 50.0
		else:
			self.reward = 0.0
# Create array of nodes to be used in search
StateArray = []
for i in range(0, rows):
	thisrow = []
	for j in range(0, cols):
		thisrow.append(State(i, j, int(matrix[i][j])))
	StateArray.append(thisrow)			


# Create functions that return the new utility or 0 if there is a wall. 
# Visit property is used for determining the final path
def UpMove(row, col):
	if row == 0:
		return 0.0
	elif StateArray[row-1][col].visit == True:
		return 0.0
	else:
		return StateArray[row-1][col].utility
def DownMove(row, col):
	if row == rows-1:
		return 0.0
	elif StateArray[row+1][col].visit == True:
		return 0.0
	else:
		return StateArray[row+1][col].utility
def RightMove(row, col):
	if col == cols-1:
		return 0.0
	elif StateArray[row][col+1].visit == True:
		return 0.0
	else:
		return StateArray[row][col+1].utility	
def LeftMove(row, col):
	if col == 0:
		return 0.0
	elif StateArray[row][col-1].visit == True:
		return 0.0
	else:
		return StateArray[row][col-1].utility


# Loop to determine utilities of each state

gamma = 0.9
delta = 100.0

while delta > Epsilon*(1-gamma)/gamma:
	
	delta = 0.0
	# Loop through each state:
	for i in range(0, rows):
		for j in range(0, cols):
			
			if StateArray[i][j].value != 5 and StateArray[i][j].value != 2:
			
				# Consider each possible action for the state, decide which action is best
				Up = UpMove(i, j)*0.8 + RightMove(i, j)*0.1 + LeftMove(i, j)*0.1
				Right = RightMove(i, j)*0.8 + UpMove(i, j)*0.1 + DownMove(i, j)*0.1
				Down = DownMove(i, j)*0.8 + RightMove(i, j)*0.1 + LeftMove(i, j)*0.1
				Left = LeftMove(i, j)*0.8 + UpMove(i, j)*0.1 + DownMove(i, j)*0.1
				maxAction = max(Up, Right, Down, Left)
				
		
				# Caluclate utility 
				U_new = StateArray[i][j].reward + gamma*maxAction
				
				
				diff = abs(U_new - StateArray[i][j].utility)
				if diff > delta:
					delta = diff
				StateArray[i][j].utility = U_new
				
		

# Collect results and print output

thisStateRow = rows-1 # starting row
thisStateCol = 0 # starting col

Path = [[thisStateRow, thisStateCol]]
UtilityPath = StateArray[thisStateRow][thisStateCol].utility
StateArray[thisStateRow][thisStateCol].visit = True
endReached = False

while endReached == False:

	Up = UpMove(thisStateRow, thisStateCol)
	Down = DownMove(thisStateRow, thisStateCol)
	Left = LeftMove(thisStateRow, thisStateCol)
	Right = RightMove(thisStateRow, thisStateCol)
	maxUtility = max(Up, Down, Left, Right)
	
	if maxUtility == Up:
		thisStateRow = thisStateRow - 1
	if maxUtility == Down:
		thisStateRow = thisStateRow + 1
	if maxUtility == Left:
		thisStateCol = thisStateCol - 1
	if maxUtility == Right:
		thisStateCol = thisStateCol + 1
	
	
	Path.append([thisStateRow, thisStateCol])
	UtilityPath = UtilityPath + StateArray[thisStateRow][thisStateCol].utility
	StateArray[thisStateRow][thisStateCol].visit = True
	
	if StateArray[thisStateRow][thisStateCol].value == 5:
		endReached = True

print "\nPath:"
print Path		
	
print "\nUtility Sum along Path:"
print UtilityPath

print

	
	






		
