examples = []

from gui import *

class Example:
	def __init__(self, name, code):
		self.name = name
		self.code = code
		examples.append(self)
	def set(self):
		code.delete(1.0, END)
		code.insert(INSERT, self.code)

Example('1-Variable Function', 
'''
#Graph a 1-Variable function

f = Function("f", "x*x", 1)
graph([f])
''')

Example('2-Variable Function', 
'''
#Graph a 2-Variable function

f = Function("f", "0.1*(x*x + y*y)", 2)
graph([f])
''')

Example('3-Variable Function', 
'''
#Graph a 3-Variable function

f = Function("f", "5 - (x*x + y*y + z*z)", 3)
graph([f])
''')

Example('4-Variable Function', 
'''
#Graph a 4-Variable function

f = Function("f", "x + 0.1*(y*y) + 0.1*(z*z*z) - sin(u)*x", 4)
graph([f])
''')

Example('3D Vector', 
'''
#Graph a 3D Vector

v1 = Vector("v1", [2.0, 2.0, 2.0])
graph([v1])
''')

Example('4D Vector', 
'''
#Graph a 4D Vector

v1 = Vector("v1", [2.0, 2.0, 2.0,2.0])
graph([v1])
''')

Example('1-Variable Parametric', 
'''
p1 = Parametric("p1", ["5*sin(t)", "5*cos(t)", "t"], 1)
graph([p1])
''')

Example('2-Variable Parametric', 
'''
p1 = Parametric("p1", ["cos(t)*(2 + cos(r))", "sin(t)*(2+cos(r))", "sin(r)"], 2)
graph([p1])
''')

Example('3-Variable Parametric', 
'''
p1 = Parametric("p1", ["t-r", "r-s", "t-s"], 3)
graph([p1])
''')

Example('2D Directional Field', 
'''
vf = VectorField("vf", ["x+y", "1"], 2)
graph([vf])
''')

Example('3D Directional Field', 
'''
vf = VectorField("vf", ["x+y", "y+z", "z"], 3)
graph([vf])
''')

Example('4D Directional Field', 
'''
vf = VectorField("vf", ["x+y+u*u", "y+z-u*u*u", "z-u"], 4)
graph([vf])
''')