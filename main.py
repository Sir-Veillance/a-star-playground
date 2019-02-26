import os

cls = lambda: os.system('cls')

class Node(object):
	def __init__(self, x, y, target, parent):
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

grid = [['oooooooooo'],
		['oooooooooo'],
		['oxxxxxxooo'],
		['oooooooooo'],
		['oooooooooo'],
		['ooooxxxxoo'],
		['oooooooooo'],
		['ooxxxooooo'],
		['oooooooooo'],
		['oooosooooo']]

start_coordinates = (4, 9)

target_x = int(input('Enter target x coordinate (0-9): '))
target_y = int(input('Enter target y coordinate (0-9): '))
cls()
end_coordinates = (target_x, target_y)

start_node = Node(start_coordinates[0], start_coordinates[1], end_coordinates, None)
