import os
import math
import time
import pygame
from pygame.locals import *

pygame.init()

window_width = 480
window_height = 480

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('A*')

# draw order: background, grid, walls, path, start/end
background = (217, 173, 124)
wall_color = (103, 77, 60)
grid_color = (162, 131, 110)
path_color = (255, 242, 223)

window.fill(background)

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
		'ooooooooooooooooooooooooooooxx',
		'ooxxxooooooooooooooooooooooooo',
		'ooooooooooxxxxxxxxoooooxxxxxxx',
		'ooooooooooooooooooooxxoooooooo',
		'oooxxxxxxxxxxxoooooooooooooooo',
		'xxoooooooooooooooxxxxxxxxxxxxo',
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
		'ooooxooooooooooooooooooooooooo',
		'ooooxooooooooooooooooooooooooo',
		'oooooooooooooosooooooooooooooo']

start_coordinates = (14, 29)

#target_x = int(input('Enter target x coordinate (0-29): '))
#target_y = int(input('Enter target y coordinate (0-29): '))
#cls()
#end_coordinates = (target_x, target_y)

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
				elif current_node.y + i == target[1] and current_node.x + j == target[0]:
					path_node = Node(current_node.x + j, current_node.y + i, target, current_node)
					not_found = False
				else:
					next_node = Node(current_node.x + j, current_node.y + i, target, current_node)
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

terminated = False

def render(window, grid, path):
	window.fill(background)

	for i in range(30):
		for j in range(30):
			if grid[i][j] == 'x':
				rect = pygame.Rect(j*16, i*16, 16, 16)
				window.fill(wall_color, rect)
			else:
				pygame.draw.line(window, grid_color, (j*16, i*16+15), (j*16+15, i*16+15), 1)
				pygame.draw.line(window, grid_color, (j*16+15, i*16+15), (j*16+15, i*16), 1)

	previous_pos = None

	for pos in path:
		if previous_pos == None:
			pass
		else:
			pygame.draw.line(window, path_color, (pos[0]*16+7, pos[1]*16+7), (previous_pos[0]*16+7, previous_pos[1]*16+7), 2)
		previous_pos = pos

	pygame.display.update()

while not terminated:
	previous_location = (0, 0)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			terminated = True
		if event.type == pygame.MOUSEMOTION:
			pos = pygame.mouse.get_pos()
			current_pos = (pos[0]//16, pos[1]//16)
			if previous_location == current_pos:
				pass
			elif grid[current_pos[1]][current_pos[0]] == 'x':
				pass
			else:
				previous_location = current_pos
				start_node = Node(start_coordinates[0], start_coordinates[1], current_pos, None)
				shortest_path = get_path(start_node, current_pos, grid)
				render(window, grid, shortest_path)
pygame.quit()

