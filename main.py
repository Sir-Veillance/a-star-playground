import os
import math

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

	def __eq__(self, other):
		if type(other) == type(self):
			return self.x == other.x and self.y == other.y
		else:
			return False

	def generate_g(self):
		if self.parent == None:
			return 0
		else:
			g = self.parent.g
			g += math.sqrt((self.parent.y - self.y)**2 + (self.parent.x - self.x)**2)
			return g

	def generate_h(self):
		return math.sqrt((self.target[1] - self.y)**2 + (self.target[0] - self.x)**2)

grid = ['oooooooooooooooooooooooooooooo',
		'ooooooooooxxxxxxoooooxxxxxxooo',
		'oxxxxxxoooooooooooxxoooooooooo',
		'ooooooooooxxoooooooooooooooooo',
		'oooooooooooooooooooooooooooooo',
		'ooooxxxxooooooxxxxxxxxxxxooooo',
		'ooooooooooooooooooooooooooooxo',
		'ooxxxooooooooooooooooooooooooo',
		'ooooooooooxxxxxxxxoooooxxxxxxx',
		'ooooooooooooooooooooxxoooooooo',
		'oooxxxxxxxxxxxoooooooooooooooo',
		'xxoooooooooooooooxxxxxxxxxxxxx',
		'oooooooooooooooooooooooxoxoooo',
		'ooooooooooxxxxxooooooooxoxoooo',
		'oooooxxxxooooooooooooooxoxoooo',
		'xxxooooooooooooooooooooooooooo',
		'oooooooooooooooooooooooooooooo',
		'xxxxxxoooooooooooooxxxxooooooo',
		'oooooooooooooooooooooooooooooo',
		'oooooooooxxxxxxxxxxxxxxxoooooo',
		'ooooooxxooooooooooooooooooxxoo',
		'oooooooooooooooooooooooooooooo',
		'xxxxxxxxxxxxxxxxoooxxxxxxxxxxx',
		'oooooooooooooooooooooooooooooo',
		'oooooooooooooooooooooooooooooo',
		'xxoooooooooxxooooooooooooooooo',
		'ooooxxxxooooxxxxooooxxxxooooxx',
		'ooooxoooooooooooooooooooooooox',
		'ooooxoooooooooooooooooooooooox',
		'oooooooooooosooooooooooooooooo']

start_coordinates = (12, 29)

target_x = int(input('Enter target x coordinate (0-29): '))
target_y = int(input('Enter target y coordinate (0-29): '))
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
				if current_node.x + i < 0 or current_node.x + i > 29:
					pass
				elif current_node.y + j < 0 or current_node.y + j > 29:
					pass
				elif current_node.x + i == current_node.x and current_node.y + j == current_node.y:
					pass
				elif current_node.x + i == end_coordinates[0] and current_node.y + j == end_coordinates[1]:
					path_node = Node(current_node.x + i, current_node.y + j, end_coordinates, current_node)
					found = True
				elif grid[current_node.y + j][current_node.x + i] != 'x':
					next_node = Node(current_node.x + i, current_node.y + j, end_coordinates, current_node)
					new_node = True
					if next_node in closed_nodes:
						new_node = False
					if new_node:
						open_nodes.append(next_node)
						open_nodes.sort(key=lambda x: x.f, reverse=False)
					else:
						pass
				else:
					pass
		closed_nodes.append(open_nodes.pop(open_nodes.index(current_node)))
		print(len(open_nodes))
		print(len(closed_nodes))

	path = []
	pathing_node = path_node
	while pathing_node.parent != None:
		path.append((pathing_node.x, pathing_node.y))
		pathing_node = pathing_node.parent

	return path

shortest_path = get_path(start_node, end_coordinates, grid)

for i in range(30):
	line = ''
	for j in range(30):
		if j == start_node.x and i == start_node.y:
			line += '\x1b[6;30;43m' + 'S' + '\x1b[0m'
		elif j == end_coordinates[0] and i == end_coordinates[1]:
			line += '\x1b[6;30;43m' + 'T' + '\x1b[0m'
		elif (j, i) in shortest_path:
			line += '\x1b[6;30;42m' + 'x' + '\x1b[0m'
		elif grid[i][j] == 'x':
			line += '\x1b[6;30;41m' + 'w' + '\x1b[0m'
		else:
			line += '-'
	print(line)

input()