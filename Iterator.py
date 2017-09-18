#coding: utf-8

import abc

class Iterator(object):

	def __init__(self, container):
		super(Object, self).__init__()
		self._container = container
		
	def __iter__(self):
		return self
		
	@abc.abstractmethod
	def next(self): pass
