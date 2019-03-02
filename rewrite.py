import os
import math
import time

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
		if isinstance(other, Node):
			return (self.x == other.x) and (self.y == other.y)
		return False

	def generate_g(self):
		if self.parent == None:
			return 0
		else:
			g = self.parent.g
			g += math.sqrt((self.parent.x - self.x)**2 + (self.parent.y - self.y)**2)
			return g

	def generate_h(self):
		return math.sqrt((self.target[0] - self.x)**2 + (self.target[1] - self.y)**2)

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
		'oooooooooooooooooooxoxoxoxoooo',
		'ooooooooooxxxxxooooxoxoxoxoooo',
		'oooooxxxxooooooooooxoxoxoxoooo',
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
		'oooooooooooooosooooooooooooooo']

start_coordinates = (14, 29)

target_x = int(input('Enter target x coordinate (0-29): '))
target_y = int(input('Enter target y coordinate (0-29): '))
cls()
end_coordinates = (target_x, target_y)

start_node = Node(start_coordinates[0], start_coordinates[1], end_coordinates, None)

def get_path(start_node, target, grid):
	open_nodes = []
	open_nodes.append(start_node)
	closed_nodes = []

	not_found = True

	while len(open_nodes) > 0 and not_found:
		current_node = open_nodes[0]
		open_nodes.pop(0)
		closed_nodes.append(current_node)
		for i in range(-1, 2):
			for j in range(-1, 2):
				if current_node.y + i < 0 or current_node.y + i > 29 or current_node.x + j < 0 or current_node.x + j > 29:
					pass
				elif i == 0 and j == 0:
					pass
				elif grid[current_node.y + i][current_node.x + j] == 'x':
					pass
				elif current_node.y + i == end_coordinates[1] and current_node.x + j == end_coordinates[0]:
					path_node = Node(current_node.x + j, current_node.y + i, end_coordinates, current_node)
					not_found = False
				else:
					next_node = Node(current_node.x + j, current_node.y + i, end_coordinates, current_node)
					if next_node in closed_nodes:
						pass
					elif next_node in open_nodes:
						if next_node.g < open_nodes[open_nodes.index(next_node)].g:
							open_nodes[open_nodes.index(next_node)] = next_node
						else:
							pass
					else:
						open_nodes.append(next_node)

		open_nodes.sort(key=lambda x: x.f, reverse=False)

	path = []
	current_node = path_node
	while current_node.parent != None:
		path.append((current_node.x, current_node.y))
		current_node = current_node.parent

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