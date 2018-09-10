# Michelle Cheng
# CS 151 Project 10
# version 5
#

import turtleTk3D 
import random as r
import sys

class TurtleInterpreter:
	initialized = False
	t = None
	
	def __init__(self, dx = 800, dy = 800):
		'''sets up a turtle window'''
		self.style = 'normal'
		self.jitterSigma = 2
		self.dotSize = 1
		if TurtleInterpreter.initialized:
			return
		global t
		t = turtleTk3D.Turtle3D(dx, dy)
		TurtleInterpreter.initialized = True
		
		t.setup(width = dx, height = dy)
		t.tracer(False)
	
	def forward(self, distance):
		if self.style == 'normal':
			t.forward(distance)
		elif self.style == 'jitter':
			(x0, y0, z0) = t.position()
			t.up()
			t.forward(distance)
			(xf, yf, zf) = t.position()
			curwidth = t.width()

			jx = r.gauss(0, self.jitterSigma)
			jy = r.gauss(0, self.jitterSigma)
			jz = r.gauss(0, self.jitterSigma)
			kx = r.gauss(0, self.jitterSigma)
			ky = r.gauss(0, self.jitterSigma)
			kz = r.gauss(0, self.jitterSigma)

			t.width(curwidth + r.randint(0, 2))
			t.goto(x0 + jx, y0 + jy, z0 + jz)
			t.down()
			t.goto(xf + kx, yf + ky, zf +kz)
			t.up()
			t.goto(xf, yf, zf)
			t.width(curwidth)
			t.down()
		elif self.style == 'jitter3':
			(x0, y0, z0) = t.position()
			t.up()
			t.forward(distance)
			(xf, yf, zf) = t.position()
			curwidth = t.width()
			
			for i in range(3):
				jx = r.gauss(0, self.jitterSigma)
				jy = r.gauss(0, self.jitterSigma)
				jz = r.gauss(0, self.jitterSigma)
				kx = r.gauss(0, self.jitterSigma)
				ky = r.gauss(0, self.jitterSigma)
				kz = r.gauss(0, self.jitterSigma)

				t.width(curwidth + r.randint(0, 2))
				t.goto(x0 + jx, y0 + jy, z0 +jz)
				t.down()
				t.goto(xf + kx, yf + ky, zf +kz)
				t.up()
				t.goto(xf, yf, zf)
				t.width(curwidth)
				t.down()
		elif self.style == 'dotted':
			incre = int(distance/10)
			
			for i in range(0, int(distance), incre):
				t.begin_fill()
				t.right(90)
				t.circle(self.dotSize)
				t.left(90)
				t.end_fill()
				t.up()
				t.forward(incre)
				t.down()
		elif self.style == 'brush':
			(x0, y0, z0) = t.position()
			t.up()
			t.forward(distance)
			(xf, yf, zf) = t.position()
			curwidth = t.width()

			
			for i in range(10):
				jx = r.gauss(0, self.jitterSigma)
				jy = r.gauss(0, self.jitterSigma)
				jz = r.gauss(0, self.jitterSigma)


				t.width(curwidth + r.randint(0, 2))
				t.goto(x0 + jx, y0 + jy, z0 + jz)
				t.down()
				t.goto(xf + jx, yf + jy, zf + jz)
				t.up()
				t.goto(xf, yf, zf)
				t.width(curwidth)
				t.down()

				
				
			
		
	def place(self, xpos, ypos, angle=None, zpos = 0, pitch = 0, roll = 0):
		'''places image in specified location'''
		t.up()
		t.goto(xpos, ypos, zpos)
		if angle is not None:
			self.orient(angle, roll, pitch)
		t.down()
	
	def orient(self, angle, roll = 0, pitch = 0):
		'''orientates image'''
		t.setheading(0)
		t.roll(roll)
		t.pitch(pitch)
		t.yaw(angle)
	
	def goto(self, xpos, ypos, zpos = 0):
		'''moves turtle mouse to specified location'''
		t.up()
		t.goto(xpos, ypos, zpos)
		t.down()
	
	def setStyle(self, s):
		self.style = s
		
	def setJitter(self, j):
		self.jitterSigma = j
	
	def setDotSize(self, d):
		self.dotSize = d
		
	def setColor(self, c):
		'''changes color of the turtle'''
		t.color(c)
	
	def setWidth(self, w):
		'''changes the width of the turtle'''
		t.width(w)
	
	def roll(self, r):
		'''changes roll value of turtle'''
		t.roll(r)
	
	def pitch(self, p):
		'''changes pitch value of turtle'''
		t.pitch(p)
	
	def yaw(self, y):
		'''changes yaw value of turtle'''
		t.yaw(y)
		
  
	def drawString(self, dstring, distance, angle):
		""" Interpret the characters in string dstring as a series
		of turtle commands. Distance specifies the distance
		to travel for each forward command. Angle specifies the
		angle (in degrees) for each right or left command. The list of 
		turtle supported turtle commands is:
		F : forward
		- : turn right
		+ : turn left
		[ : save position, heading
		] : restore position, heading
		"""
		
		stack = []
		colorstack = []
		
		modstring = ''
		modval = None
		modgrab = False

		for c in dstring:
			if c == '(':
				modstring = '' 
				modgrab = True
				continue
			elif c == ')':
				modval = float(modstring)
				modgrab = False
				continue
			elif modgrab == True:
				modstring += c
				continue
				
			if c == 'F' or c == 'f':
				if modval == None:
					self.forward(distance)
				else:
					self.forward(distance * modval)
			elif c == 'B':
				t.backward(distance)
			elif c == '!':
				if modval == None:
					w = t.width()
					if w > 1:
						t.width(w-1)
				else:
					t.width(modval)
			elif c == '-':
				'''yaw the turtle right by angle degrees'''
				if modval == None:
					t.yaw(-1*angle)
				else:
					t.yaw(-1*modval)
			elif c == '+':
				'''yaw the turtle left by angle degrees'''
				if modval == None:
					t.yaw(angle)
				else:
					t.yaw(modval)
			elif c == '&':
				'''pitch turtle down by angle degrees'''
				if modval == None:
					t.pitch(angle)
				else:
					t.pitch(modval)
			elif c == '^':
				'''pitch turtle up by angle degrees'''
				if modval == None:
					t.pitch(-1*angle)
				else:
					t.pitch(-1*modval)	
			elif c == '\\':
				'''roll turtle to the right by angle degrees'''
				if modval == None:
					t.roll(angle)
				else:
					t.roll(modval)
			elif c == '/':
				'''roll turtle to the left by angle degrees'''
				if modval == None:
					t.roll(-1*angle)
				else:
					t.roll(-1*modval)			
			elif c == '[':
			  stack.append(t.position())
			  stack.append(t.heading())
			  stack.append(t.width())
			elif c == ']':
			  t.up()
			  t.width(stack.pop())
			  t.setheading(stack.pop())
			  t.goto(stack.pop())
			  t.down()
			elif c == 'L':
				stack.append(t.heading())
				colorstack.append(t.color())
				t.right(r.randint(0,180))
				t.color(r.randint(60,150)/255, r.randint(100,200)/255, r.randint(0,50)/255)
				t.begin_fill()
				t.circle(distance,180)
				t.right(90)
				t.backward(distance*2)
				t.end_fill()
				hold = stack.pop()
				t.setheading(hold)
				t.color(colorstack.pop())
			elif c == '<':
				colorstack.append(t.color())
			elif c == '>':
				t.color(colorstack.pop())
			elif c == 'g':
				t.color(0.15, 0.5, 0.2)
			elif c == 'y':
				t.color(0.8, 0.8, 0.3)
			elif c == 'r':
				t.color(0.7, 0.2, 0.3)
			elif c == '{':
				t.begin_fill()
			elif c == '}':
				t.end_fill()
			modval = None  

		t.update()

	def hold(self):
		""" holds the screen open until the user clicks or types 'q' """

		t.mainloop()  