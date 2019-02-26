class Node(object):
	def __init__(self, x, y, target, parent, g, h):
		self.x = x
		self.y = y
		self.target = target
		self.parent = parent
		self.g = self.generate_g()
		self.h = self.generate_h()
		self.f = g + h

	def generate_g(self):
		g = 0
		previous_node = self.parent
		while previous_node.parent != None:
			g += 1
			previous_node = previous_node.parent
		return g

	def generate_h(self):
		return = (target.y - self.y)**2 + (target.x - self.x)**2