#!/usr/bin/python 

## This file contains the function for the second heuristic to be used in main.py

## Emily Stohl
## 9/18/2015
## Homework #3 (Programming Assignment 2)

# Heuristic 2

# This heuristic calculates the cost of the moves to the end assuming 
# there are no walls or mountains. It will maximize the number of diagonal 
# moves, then move horizontally or vertically to get to the end point. 
# Then, the number of diagonal moves is multiplied by 14 and the number of 
# horizontal/vertical moves is multiplied by 10, which are the costs to make 
# each one of these moves.


def heuristic(current_row, current_col, end_row, end_col):
	H_dist = abs(end_row - current_row)
	V_dist = abs(end_col - current_col)
	
	NumDiagMoves = min(H_dist, V_dist)
	NumSideMoves = abs(H_dist-V_dist)
	
	ans = NumSideMoves*10 + NumDiagMoves*14
	
	return ans

