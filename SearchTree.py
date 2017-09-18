#coding: utf-8

from SearchableContainer import SearchableContainer
from Tree import Tree
import abc

class SearchTree(SearchableContainer, Tree):

	def __init__(self):
		super(SearchTree, self).__init__()
		
	@abc.abstractmethod
	def getMin(self): pass
	
	min = property(
		fget = lambda self: self.getMin())
	
	@abc.abstractmethod
	def getMax(self): pass
	
	max = property(
		fget = lambda self: self.getMax())
	
	@abc.abstractmethod
	def preOrder(self): pass
	
	@abc.abstractmethod
	def postOrder(self): pass
	
	@abc.abstractmethod
	def inOrder(self): pass
	
	

