#coding: utf-8

from Container import Container
import abc

class Tree(Container):
	
	def __init__(self):
		super(Tree, self).__init__()
	
	@abc.abstractmethod
	def getKey(self): pass
	
	key = property(
		fget = lambda self: self.getKey())	
	
	@abc.abstractmethod
	def getHeight(self): pass
	
	height = property(
		fget = lambda self: self.getHeight())
	
	@abc.abstractmethod
	def getDegree(self): pass
	
	degree = property(
		fget = lambda self: self.getDegree())
	
	@abc.abstractmethod
	def getIsLeaf(self): pass
	
	isLeaf = property(
		fget = lambda self: self.getIsLeaf())
		
