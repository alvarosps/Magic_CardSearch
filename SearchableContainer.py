#coding: utf-8

from Container import Container
import abc

class SearchableContainer(Container):

	def __init__(self):
		super(SearchableContainer, self).__init__()
	
	@abc.abstractmethod	
	def insert(self, obj): pass
	
	@abc.abstractmethod
	def remove(self, obj): pass
	
	@abc.abstractmethod
	def find(self, obj): pass
	
	
