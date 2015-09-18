#!/usr/bin/python 

## This file contains the function for the first heuristic to be used in main.py

## Emily Stohl
## 9/18/2015
## Homework #3 (Programming Assignment 2)

# Heuristic 1 
# Manhattan distance 

def heuristic(current_row, current_col, end_row, end_col):
	H_dist = abs(end_row - current_row)
	V_dist = abs(end_col - current_col)
	return H_dist + V_dist
