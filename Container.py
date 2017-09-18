#coding: utf-8

from Iterator import Iterator
import abc

class Container(object):

	def __init__(self):
		super(Container, self).__init__()
		self._count = 0
		
	def getCount(self):
		return self._count
		
	count = property(
		fget = lambda self: self.getCount())
		
	def getIsEmpty(self):
		return self.count == 0
		
	isEmpty = property(
		fget = lambda self: self.getIsEmpty())
		
	@abc.abstractmethod
	def __iter__(self): pass
	
	@abc.abstractmethod
	def __contains__(self): pass
		
	@abc.abstractmethod
	def purge(self): pass		
	
