# Michelle Cheng
# CS 151 Project 10
# Version 5
#

import turtle_interpreter as ti

class Shape:
	'''creates an object Shape'''
	def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '', style = 'normal', jitterSigma = 2, lineWidth = 1):
		self.distance = distance
		self.angle = angle
		self.color = color
		self.string = istring
		self.style = style
		self.jitterSigma = jitterSigma
		self.lineWidth = lineWidth
		self.dotSize = 1
		
	def setColor(self, c):
		self.color = c
	
	def setDistance(self, d):
		self.distance = d
	
	def setAngle(self, a):
		self.angle = a
	
	def setString(self, s):
		self.string = s
	
	def setStyle(self, nStyle):
		self.style = nStyle
	
	def setJitter(self, nJitter):
		self.jitterSigma = nJitter
	
	def setDotSize(self, dotSize):
		self.dotSize = dotSize
	
	def setWidth(self, nWidth):
		self.lineWidth = nWidth
		
	def draw(self, xpos, ypos, scale = 1, orientation = 0, zpos = 0, pitch = 0, roll = 0):
		obj = ti.TurtleInterpreter()
		obj.place(xpos, ypos, orientation, zpos, pitch, roll)
		obj.setColor(self.color)
		obj.setStyle(self.style)
		obj.setJitter(self.jitterSigma)
		obj.setDotSize(self.dotSize)
		obj.setWidth(self.lineWidth)
		obj.drawString(self.string, self.distance*scale, self.angle)
		
class Square(Shape):
	'''creates Shape child object Square'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False ):		
		if fill:
			Shape.__init__(self, distance, 90, color, '{F-F-F-F-}')
		else:
			Shape.__init__(self, distance, 90, color, 'F-F-F-F-')
		

class Triangle(Shape):
	'''creates Shape child object Triangle'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False):
		if fill:
			Shape.__init__(self, distance, 120, color, '{F-F-F-}')
		else:
			Shape.__init__(self, distance, 120, color, 'F-F-F-')
		
class Rectangle(Shape):
	'''creates Shape child object Rectangle'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False):
		if fill:
			Shape.__init__(self, distance, 90, color, '{F-FF-F-FF-}')
		else:
			Shape.__init__(self, distance, 90, color, 'F-FF-F-FF-')
		
		
class Star(Shape):
	'''creates Shape child object Star'''
	def __init__(self, distance = 100, color = ("Yellow"), nofill = False):
		if nofill:
			Shape.__init__(self, distance, 30, color, '++F++F++++F++F+++')
		else:
			Shape.__init__(self, distance, 30, color, '{++F++F++++F++F+++}')

class Hexagon(Shape):
	'''creates Shape child object Hexagon'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False):
		if fill:
			Shape.__init__(self, distance, 60, color, '{F-F-F-F-F-F-}')
		else:
			Shape.__init__(self, distance, 60, color, 'F-F-F-F-F-F-')

class Curve(Shape):
	'''creates Shape child object Curve'''
	def __init__(self, size = 10, color = (0, 0, 0), len = 6 ):
		Shape.__init__(self, size, 10, color,  'F(20)-'*len   )
		
class Snowflake(Shape):
	'''creates Shape child object Snowflake with specified amount of branches'''
	def __init__(self, size = 10, color = (0, 0, 0), branches = 6 ):
		incre = str(360/branches)
		branch = '(3)FB(45)-FB(90)+FB(45)-B(45)-FB(90)+FB(45)-B('+ incre + ')+'
		
		def makeFlake(branches):
			fullBranch = ''
			for i in range(branches):
				fullBranch += branch
			return fullBranch

		Shape.__init__(self, size, 10, color,  makeFlake(branches)  )

class Box(Shape):
	'''creates Shape child object 3d box'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False):
		if fill:
			Shape.__init__(self, distance, 90, color, '{F-F-F-F}^{F^F}{[^F]-F}{[^F]-F}{^FB-F}')
		else:
			Shape.__init__(self, distance, 90, color, 'F-F-F-F^F^F[^F]-F[^F]-F^FB-F')

class Pyramid(Shape):
	'''creates Shape child object 3d pyramid'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False):
		Shape.__init__(self, distance, 90, color, 'F[(135)-(45)&F](90)-F[(135)-(45)&F](90)-F[(135)-(45)&F](90)-F[(135)-(45)&F](90)-F')	
		
class Octahedron(Shape):
	'''creates Shape child object 3d octahedron'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False):
		Shape.__init__(self, distance, 90, color, 'F[[(135)-(45)&F](135)-(45)^F](90)-F[[(135)-(45)&F](135)-(45)^F](90)-F[[(135)-(45)&F](135)-(45)^F](90)-F[[(135)-(45)&F](135)-(45)^F](90)-F')

class Teardrop(Shape):
	'''creates Shape child object 3d teardrop'''
	def __init__(self, distance = 100, color = (0, 0, 0), fill = False):
		str = 'F'
		if fill:
			for i in range(5):
				str += '{[(64)\\(72)-F(72)-F(72)-F[(72)-F]}{(250)/(70)-F(80)-FF(130)-FF](72)+F}'
		else:
			for i in range(5):
				str += '[(64)\\(72)-F(72)-F(72)-F[(72)-F](250)/(70)-F(80)-FF(130)-FF](72)+F'
		Shape.__init__(self, distance, 90, color, str)
		
			

def test():
	one = Box()
	two = Pyramid()
	three = Octahedron()
	four = Teardrop()
	one.setStyle('brush')
	four.setStyle('jitter3')
	one.draw(-100, 0)
	two.draw(100, 200)
	three.draw(100, 0)
	four.draw(-100, 200, scale = .5)
	
	
	ti.TurtleInterpreter().hold()


if __name__ == "__main__":
	test()
		
