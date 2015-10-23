#!/usr/bin/python 

## Emily Stohl
## 10/23/2015
## Programming Assignment 6
## Bayesian Nets

# Code does not currently run


## Import command line input 
import getopt, sys
from functions import *

# Code modified from Professor Hoenigman's code:
def main():
	
	BNet = BayesNet()
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	for o, a in opts:
		if o in ("-p"):
			BNet.setPrior(a[0], float(a[1:]))
		elif o in ("-m"):
			BNet.calcMarginal(a)
		elif o in ("-g"):
			# Could not use "|" for conditional call
			# Instead use "/" to represent "|" ex: -gc/s calculates P(c | s)
			p = a.find("/")
			BNet.calcConditional(a[:p], a[p+1:])
		elif o in ("-j"):				
			BNet.calcJoint(a)
		else:
			assert False, "unhandled option"
		

if __name__ == "__main__":
	main()


