# Michelle Cheng
# CS 151 Project 10
#

import turtle_interpreter as ti
import shapes as s
import lsystem as ls
import random as r
import tree

def task2():
	'''create scene of tree surrounded by boxes'''
	x = ti.TurtleInterpreter()
	
	#creates ground
	sq = s.Square(fill = True)
	sq.setColor('#d6f0f9')
	sq.draw(0, -200, scale = 1.5, zpos = 0, roll = 90)
	sq.draw(-150, -200, scale = 1.5, zpos = 0, roll = -90)
	sq.setColor('#f7e3f4')
	sq.draw(0, -200, scale = 1.5, zpos = 0, roll = -90)
	sq.draw(-150, -200, scale = 1.5, zpos = 0, roll = 90)
	
	
	#create tree
	tree1 = tree.Tree(20, filename = "systemZ.txt")
	tree1.setIterations(4)
	tree1.draw(0, -200, scale = 1.0, zpos = 0)
	
	#creates boxes
	sq2 = s.Box()
	colors = ['#8ee28c', '#167714', '#55c153', '#29a327']
	sq3 = s.Octahedron()
	sq4 = s.Pyramid()
	
	for i in range(0, 360, 30):
		x0 = r.randint(-70, 30)
		y0 = r.randint(-200, -150)
		sc = r.randint(1, 5)
		pick = r.choice(colors)
		roll0 = r.randint(-180, 180)
		sq2.setColor(pick)
		sq2.draw(x0, y0, scale = sc/5, roll = roll0)
	
	for i in range(4):
		x0 = r.randint(-100, 100)
		x1 = r.randint(-100, 100)
		y0 = r.randint(-150, 100)
		y1 = r.randint(-150, 100)
		sc = r.randint(1, 3)
		pick = r.choice(colors)
		roll0 = r.randint(-180, 180)
		sq3.setColor(pick)
		sq3.draw(x0, y0, scale = sc/5, roll = roll0)
		sq4.setColor(pick)
		sq4.draw(x1, y1, scale = sc/5, roll = roll0)
	x.hold()

def task3():
	'''create scene of a treasure box'''
	x = ti.TurtleInterpreter()
	#box outline 
	box1 = s.Box()
	box1.draw(0, 0, scale = 2)
	
	#center thing
	tree1 = tree.Tree(iterations = 7, filename = 'systemZ2.txt')
	tree1.draw(100, -200, scale = 2.5, zpos = 100)
	
	#middle band of boxes
	box2 = s.Box(fill = True)
	colors1 = ['#e3f0f7', '#c5e6f7', '#eff6f9', '#e5f3f9']
	for i in range(0, 200, 25):
		box2.setColor(r.choice(colors1))
		box2.draw(i, -100, scale = .25)
		box2.draw(175, -100, scale = .25, zpos = i )
		box2.draw(0, -100, scale = .25, zpos = i )
		box2.draw(i, -100, scale = .25, zpos = 175 )
	
	#center ornament
	tears = s.Teardrop()
	tears.setColor('#2af7db')
	tears.setDotSize(3)
	tears.draw(90, -130, scale = .2, zpos = 200)
	
	#bottom mosaic of pyramids
	py = s.Pyramid()
	py.setStyle('jitter3')
	colors2 = ['#fcc4d9', '#fce3ec', '#f796b9', '#c6f796', '#e0f9c7', '#eaf7de']
	for i in range(0, 200, 25):
		for b in range(0, 200, 25):
			py.setColor(r.choice(colors2))
			py.draw(i, -200, scale = .25, zpos = b+25, roll = 90)

	x.hold()



if __name__ == "__main__":
	task2()