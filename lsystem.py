# Michelle Cheng
# CS 151 Project 10
# version 4
#

import sys
import random as r

class Lsystem:

	def __init__( self, filename = None ):
		'''creates an Lsystem object with a base and rules'''
		self.base = ''
		self.rules = {}
		if filename != None:
			self.read(filename)

	def setBase(self, newbase):
		'''sets the base to a new value'''
		self.base = newbase
	
	def getBase(self):
		'''returns the value of the Lsystem base'''
		return self.base
		
	def getRule(self, key):
		'''returns the value of the Lsystem rule at a specific index'''
		if self.rules.get(key) != None: #if key in self.rules.keys():
			return self.rules[key]
		
	def addRule(self, newrule):
		'''adds a new rule to the Lsystem'''
		self.rules[newrule[0]] = newrule[1:]
		
	def numRules(self):
		'''retuns the number of rules'''
		return len(self.rules)
		
	def read( self, filename ):
		""" Create an L-system list by reading in the specified file """
		fp = open(filename, "rU")
		lines = fp.readlines()
		fp.close()
	
		for i in lines:
			words = i.split()
			if words[0] == 'base':
				self.setBase(words[1])
			elif words[0] == 'rule':
				self.addRule(words[1:])
				
	def replace(self, istring):
		""" Replace all characters in the istring with strings from the
			right-hand side of the appropriate rule. This version handles
			parameterized rules.
		"""
		tstring = ''
		parstring = ''
		parval = None
		pargrab = False

		for c in istring:
			if c == '(':
				# put us into number-parsing-mode
				pargrab = True
				parstring = ''
				continue
			# elif the character is )
			elif c == ')':
				# put us out of number-parsing-mode
				pargrab = False
				parval = float(parstring)
				continue
			# elif we are in number-parsing-mode
			elif pargrab:
				# add this character to the number string
				parstring += c
				continue

			if parval != None:
				key = '(x)' + c
				if key in self.rules:
					replacement = r.choice(self.rules[key])
					tstring += self.substitute( replacement, parval )
				else:
					if c in self.rules:
						replacement = r.choice(self.rules[c])
						tstring += self.insertmod( replacement, parstring, c )
					else:
						tstring += '(' + parstring + ')' + c
				parval = None
			else:
				if c in self.rules:
					tstring += r.choice(self.rules[c])
				else:
					tstring += c

		return tstring
	
	def substitute(self, sequence, value ):
		""" given: a sequence of parameterized symbols using expressions
			of the variable x and a value for x
			substitute the value for x and evaluate the expressions
		"""

		expr = ''
		exprgrab = False

		outsequence = ''

		for c in sequence:

			# parameter expression starts
			if c == '(':
				# set the state variable to True (grabbing the expression)
				exprgrab = True
				expr = ''
				continue

			# parameter expression ends
			elif c == ')':
				exprgrab = False
				# create a function out of the expression
				lambdafunc = eval( 'lambda x: ' + expr )
				# execute the function and put the result in a (string)
				newpar = '(' + str( lambdafunc( value ) ) + ')'
				outsequence += newpar

			# grabbing an expression
			elif exprgrab:
				expr += c

			# not grabbing an expression and not a parenthesis
			else:
				outsequence += c 

		return outsequence

	def insertmod(self, sequence, modstring, symbol):
		""" given: a sequence, a parameter string, a symbol 
			inserts the parameter, with parentheses, 
			before each
			instance of the symbol in the sequence
		"""
		tstring = ''
		for c in sequence:
			if c == symbol:
				# add the parameter string in parentheses
				tstring += '(' + modstring + ')'
			tstring += c
		return tstring
	
	def buildString(self, iterations):
		''' Return a string generated by applying the L-system rules for specified iterations '''
		nstring = self.getBase()
		for i in range(iterations):
			nstring = self.replace(nstring)
		return nstring
		
	def __str__(self):
		str = 'base ' + self.base
		for i in self.rules:
			str += '\n' + 'rule ' + i[0] + ' -> ' + i[1]
		return str
		
def main(argv):

	if len(argv) < 2:
	  print('Usage: lsystem.py <filename>')
	  exit()

	filename = argv[1]
	iterations = 2

	lsys = Lsystem()

	lsys.read( filename )

	print( lsys )
	print( lsys.getBase() )
	for i in range( lsys.numRules() ):
	  rule = lsys.getRule(i)
	  print( rule[0] + ' -> ' + rule[1] )

	lstr = lsys.buildString( iterations )
	print( lstr )

	return

if __name__ == "__main__":
	main(sys.argv)
		

	