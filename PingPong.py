#!/usr/bin/env python

try:
	import pygame
	from madame import Scene
except ImportError, err:
	print "Couldn't load module: %s" % (err)
	sys.exit(2)

class PingPong(Scene):

	def _start():
		self.paused = false

		#player_left
		#player_right
		#ball

	def _draw(self, dt):
		pass

	def _event(self, event):
		#manage movements
		pass

	def _update(self, dt):
		pass


