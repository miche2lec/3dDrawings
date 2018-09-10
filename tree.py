# Michelle Cheng
# CS 151 Project 9
# version 5
#

import lsystem as ls
import shapes as s
import turtle_interpreter as ti
import sys

class Tree(s.Shape):
	'''Takes an Lsystem file for a tree and creates an object Tree'''
	def __init__(self, distance = 5, angle = 22.5, color = (0.5, 0.4, 0.3), iterations = 3, filename = None):
		s.Shape.__init__(self, distance, angle, color)
		self.iterations = iterations
		self.lsys = ls.Lsystem(filename)
		
	def setIterations(self, iterations):
		self.iterations = iterations
		
	def read(self, filename):
		ls.read(filename)
		
	def draw(self, xpos, ypos, scale = 1, orientation = 90, zpos = 0, pitch = 0, roll = 0):
		self.string = self.lsys.buildString(self.iterations)
		super().draw(xpos, ypos, scale, orientation, zpos, pitch, roll)
		
		
		

def test():

	tree1 = Tree(iterations = 5, filename = 'systemJ.txt')
	tree1.draw(0, 0)
	tree1.draw(100, 100)
	tree1.draw(-100,-100)
	ti.TurtleInterpreter().hold()


if __name__ == "__main__":
	test()
	
