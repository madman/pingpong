#!/usr/bin/env python

try:
	import os, time, pygame
	from pygame.locals import *
except ImportError, err:
	print "couldn't load module. %s" % (err)
	sys.exit(2)


class Loader:
	"""Load game resouces"""

	def __init__(self,
				data_dir = 'data',
				image_dir = 'image'):
		self.data_dir = data_dir
		self.image_dir = image_dir

	def image(self, name):
		""" Load image and return image object"""
		
		fullname = os.path.join(self.data_dir, os.path.join(self.image_dir, name))
		
		try:
			image = pygame.image.load(fullname)
			if image.get_alpha() is None:
				image = image.convert()
			else:
				image = image.convert_alpha()
		
		except pygame.error, message:
			print 'Cannot load image:', fullname
			raise SystemExit, message
		
		return image, image.get_rect()


if __name__ == '__main__':
	pygame.init()
	pygame.display.set_mode((640,480))
	loader = Loader()
	pygame.display.set_icon(loader.image('icon.png'))
	pygame.display.set_caption("MADAME (MAD library for pygAME)")
	time.sleep(10)