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
		self.f = self.g + self.h

	def generate_g(self):
		g = 0
		previous_node = self.parent
		if previous_node == None:
			return g
		while previous_node.parent != None:
			g += 1
			previous_node = previous_node.parent
		return g

	def generate_h(self):
		return (self.target[1] - self.y)**2 + (self.target[0] - self.x)**2

grid = ['oooooooooo',
		'oooooooooo',
		'oxxxxxxooo',
		'oooooooooo',
		'oooooooooo',
		'ooooxxxxoo',
		'oooooooooo',
		'ooxxxooooo',
		'oooooooooo',
		'oooosooooo']

start_coordinates = (4, 9)

target_x = int(input('Enter target x coordinate (0-9): '))
target_y = int(input('Enter target y coordinate (0-9): '))
cls()
end_coordinates = (target_x, target_y)

start_node = Node(start_coordinates[0], start_coordinates[1], end_coordinates, None)

def get_path(start_node, end_coordinates, grid):
	open_nodes = []
	open_nodes.append(start_node)
	closed_nodes = []

	found = False

	while len(open_nodes) > 0 and not found:
		current_node = open_nodes[0]
		for i in range(-1, 2):
			for j in range(-1, 2):
				if current_node.x + i < 0 or current_node.x + i > 9:
					pass
				elif current_node.y + j < 0 or current_node.y + j > 9:
					pass
				elif current_node.x + i == current_node.x and current_node.y + j == current_node.y:
					pass
				elif current_node.x + i == end_coordinates[0] and current_node.y + j == end_coordinates[1]:
					path_node = Node(current_node.x + i, current_node.y + j, end_coordinates, current_node)
					found = True
				elif grid[current_node.y + j][current_node.x + i] != 'x':
					open_nodes.append(Node(current_node.x + i, current_node.y + j, end_coordinates, current_node))
					open_nodes.sort(key=lambda x: x.f, reverse=False)
				else:
					pass
		closed_nodes.append(open_nodes.pop(open_nodes.index(current_node)))


	path = []
	pathing_node = path_node
	while pathing_node.parent != None:
		path.append((pathing_node.x, pathing_node.y))
		pathing_node = pathing_node.parent

	return path

shortest_path = get_path(start_node, end_coordinates, grid)

for i in range(10):
	line = ''
	for j in range(10):
		if j == start_node.x and i == start_node.y:
			line += 'S'
		elif j == end_coordinates[0] and i == end_coordinates[1]:
			line += 'T'
		elif (j, i) in shortest_path:
			line += 'x'
		elif grid[i][j] == 'x':
			line += 'w'
		else:
			line += '-'
	print(line)
