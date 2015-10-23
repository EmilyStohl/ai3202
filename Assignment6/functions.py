#!/usr/bin/python 

## Emily Stohl
## 10/23/2015
## Programming Assignment 6
## Bayesian Nets

# This file contains all files and function that are used in main.py
# main.py takes the command line input and calls a function from this file

class BayesNode:
	def __init__(self, BoolVal, prob, parents, children, CondTable):
		self.boolval = BoolVal
		self.prob = prob # Probability that bool == True, low, or pos. Will be 1 if bool val equals these. 2.0 if unknown
		self.parents = parents
		self.children = children
		self.CondTable = CondTable
	def SetPrior(self, val):
		self.prob =  val #probability of true, low, or pos, will be 1 or 0 if value is known

	

class BayesNet:
	def __init__(self):
		self.BNet = { 'P': BayesNode(None, 0.9, [], ['C'], {}),
			         'S': BayesNode(None, 0.3, [], ['C'], {}),
			         'C': BayesNode(None, 2.0, ['P', 'S'], ['D','X'], {'HT': 0.05, 'HF': 0.02, 'LT': 0.03, 'LF': 0.001}),  # P(C=T | P,S))
			         'D': BayesNode(None, 2.0, ['C'], [], {'T': 0.65, 'F': 0.3}),
			         'X': BayesNode(None, 2.0, ['C'], [], {'T': 0.9, 'F': 0.2})} # P(X = pos | C)
		
	def ReturnLetter(self, letter): # returns a capital version of the letter
		if letter == 'p' or letter == 'P':
			return 'P'
		if letter == 's' or letter == 'S':
			return 'S'
		if letter == 'c' or letter == 'C':
			return 'C'
		if letter == 'd' or letter == 'D':
			return 'D'
		if letter == 'x' or letter == 'X':
			return 'X'
		
	def setPrior(self, Var, Prob_val): # used with the -p tag
		if Var == 'S' or Var == 's':
			self.BNet['S'].SetPrior(Prob_val)
		if Var == 'P' or Var == 'p':
			self.BNet['P'].SetPrior(Prob_val)	
	def setProb(self, Var):
		self.BNet[Var].boolval = 1
		self.BNet[Var].prob = 1.0
	
	def CalcJoint(self, CondList):
		# CondList is a list of variables
		Prod = 1.0
		while CondList != []:
			i = CondList.pop()
			Var = self.ReturnLetter(i)
			

			Prod = Prod*self.Cond(Var, CondList)

			
	def Cond(self, VarLetter, CondList):
		if CondList == []:
			return self.BNet[VarLetter].prob
		if VarLetter == 'C':
			pass

		return 1.0
			

		
	def calcConditional(self, FindProb, Conditions):
		
		if FindProb == 's' or FindProb == 'p' or FindProb == 'd' or FindProb == 'x' or FindProb == 'c': 
		# Finding a single probability value
			CondList1 = []	
			CondList2 = []
			for i in Conditions:
				Var = self.ReturnLetter(i)
				self.setProb(Var)
				CondList1.append(Var)
				CondList2.append(Var)
				
			JointConditions = self.CalcJoint(CondList2)
			CondList1.append(self.ReturnLetter(FindProb))
			JointAll = self.CalcJoint(CondList1)
			CondProb = JointAll/JointConditions
			
		
			return CondProb
		
		if FindProb == 'S' or FindProb == 'P' or FindProb == 'D' or FindProb == 'X' or FindProb == 'C': 
		# Finding a probablility distibution
			pass
		
			

			
	def calcMarginal(self, a):  
		if a == 'p':
			print("Prob(P = Low) = " + str(self.BNet['P'].prob))
		elif a == 's':
			print("Prob(S = True) = " + str(self.BNet['S'].prob))
		elif a == 'c':
			pass
		elif a == 'x':
			pass
		elif a == 'd':
			pass
		elif a == 'P':
			print("Prob(P = Low) = " + str(self.BNet['P'].prob))
			print("Prob(P = High) = " + str(1 - self.BNet['P'].prob))
		elif a == 'S':
			print("Prob(S = True) = " + str(self.BNet['S'].prob))
			print("Prob(S = False) = " + str(1 - self.BNet['S'].prob))
		elif a == 'C':
			pass
		elif a == 'X':
			pass
		elif a == 'D':
			pass
		else: 
			print("Variable " + a + " not found")
		
			
	def calcJoint(self, a):
		ArgList = []
		for i in a:
			ArgList.append(i)
		
		return
		
			    
			    
			    
			    

			
		    
