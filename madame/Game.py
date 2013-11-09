#!/usr/bin/env python

try:
	import pygame
	from Loader import Loader
except ImportError, err:
	print "couldn't load module. %s" % (err)
	sys.exit(2)

class Game(object):
	"""Game classor Game"""
	__scenes = []

	def __init__(self,
				width = 640,
				height = 480
				color = (255, 255, 255)
				fps = 40,
				loader = Loader()):
		
		pygame.init();
		
		self.set_display(width, height)

		self.fps		= fps
		self.__loader	= loader
		self.__display.fill(color)
		pygame.display.flip()

	def add_scene(self, scene):
		self.__scenes.append(scene)

	def set_display(self, width, height):
		self.__display = pygame.display.set_mode((width, height))

	def set_caption(self, title = None, icon = None):
		if title == None:
			pygame.display.set_caption("game")
		else:
			pygame.display.set_caption(title)

		if icon != None:
			pygame.display.set_icon(self.__manager.get_image(icon))

	def game_loop(self):
		while self.scene != None:
			clock = pygame.time.Clock()
			dt    = 0
			self.scene.start(self.__display, self.__loader)

			while not self.scene.is_end():
				self.scene.loop(dt)
				pygame.display.flip()
				dt = clock.tick(self.fps)

			if len(self.__scenes) > 0
				self.scene = self.__scenes.pop()
			else:
				self.scene = None