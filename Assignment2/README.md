Emily Stohl
Assignment 2
CSCI 3202



Command Line:

The program requires two command line inputs after the program name. 
The first input is the file name of the world text file, ie. World1.txt or 
World2.txt
The second input is the number of the heuristic to be used, where heuristic 1 
is the Manhattan distance and heuristic 2 is the heuristic I created.

example 1: python main.py World1.txt 1 
This will perform the search on World 1 using the first heuristic (Manhattan 
distance)

example 1: python main.py World2.txt 2
This will perform the search on World 2 using the second heuristic 




Heuristic:

My heuristic calculates the lowest cost to reach the end point from the current 
point if it is assumed that there are no walls or mountains. It will determine 
the maximum number of diagonal moves possible because these are cheaper than 1 
horizontal move and 1 vertical move, then use horizontal or vertical moves to 
reach the end point. The number of diagonal moves will be multiplied by 14 and 
the number of horizontal/vertical moves will be multiplied by 10. This 
heuristic will give a value closer to the actual cost to travel to the end 
point than the Manhattan distance. 

Equations:
H_distance = the absoulte horizontal distance between the end point and the 
current location
V_distance = the absoulte vertical distance between the end point and the 
current location
Num_Diagonal_Moves = min(H_distance, V_distance)
Num_Side_Moves = abs(H_distance - V_distance)
heuristic2 = Num_Diagonal_Moves*14 + Num_Side_Moves*10

Compared to Manhattan Distance Heuristic (heuristic 1):
In World 1, heuristic 2 resulted in the same path as heuristic 1. However, 
heristic 2 evaluated fewer locations, with heuristic 1 evaluating 59 locations 
and heuristic 2 evaluating 24 locations.
In World 2, heuristic 2 gave a slightly different path that had a cost of 142, 
compared to a path with a cost of 144 for heuristic 1. Heuristic 2 also 
required less location evaluations, with 32 locations evaluated compared to 56 
locations evaluated for heuristic 1. So in both distance cost and locations 
evaluated, heuristic 2 did better. 