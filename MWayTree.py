#coding: utf-8

from SearchTree import SearchTree
from Array import Array
import abc
import random

class MWayTree(SearchTree):
	
	
	def __init__(self, t):
		assert t >= 1
		super(MWayTree, self).__init__()
		self._t = t
		self._keyLimit = 2 * t	
		self._keys = Array(self._keyLimit)
		self._subTrees = Array(self._keyLimit + 1)
		
	def getT(self):
		return self._t
		
	t = property(
		fget = lambda self: self.getT())
		
	def getKeyLimit(self):
		return self._keyLimit
		
	keyLimit = property(
		fget = lambda self: self.getKeyLimit())
		
		
	def getIsFull(self):
		return self.count == self.keyLimit
		
	isFull = property(
		fget = lambda self: self.getIsFull())
		
	def getMax(self):
		if self.isEmpty:
			raise ValueError
		if self._subTrees[self.count].isEmpty:
			return self._keys[self.count - 1]
		else:
			return self._subTrees[self.count].max
			
	def getMin(self):
		if self.isEmpty:
			raise ValueError
		if self._subTrees[0].isEmpty:
			return self._keys[0]
		else:
			return self._subTrees[0].min
			

	def getIsLeaf(self):
		i = 0
		while i <= self.count:
			if not self._subTrees[i].isEmpty:
				return False
			i += 1
		return True

	isLeaf = property(
		fget = lambda self: self.getIsLeaf())

	def purge(self):
		self._count = 0
		self._keys.purge()
		self._subTrees.purge()

		
		
	def findIndex(self, obj):
		right = self.count
		left = 0
		while left < right:
			middle = int((left + right) / 2)
			if self._keys[middle] > obj:
				right = middle
			elif self._keys[middle] < obj:
				left = middle + 1
			else:
				return middle
		return left
		
	def find(self, obj):
		if self.isEmpty:
			raise Exception("Empty tree")
		index = self.findIndex(obj)
		if self._keys[index] == obj:
			return self._keys[index]
		else:
			return self._subTrees[index].find(obj)


	

	
	
	def insert(self, obj):
		if self.isEmpty:
			self._keys[0] = obj
			self._subTrees[0] = MWayTree(self.t)
			self._subTrees[1] = MWayTree(self.t)
			self._count = 1
		else:
			index = self.findIndex(obj)
		
			if index < self.keyLimit and self._keys[index] == obj:
				return
			if not self.isFull:
				i = self.count
				while i > index:
					self._keys[i] = self._keys[i - 1]
					self._subTrees[i + 1] = self._subTrees[i]
					i -= 1
				self._keys[index] = obj
				self._subTrees[index + 1] = MWayTree(self.t)
				self._count += 1
			else:
				self._subTrees[index].insert(obj)
		

	def remove(self, obj):
		if self.isEmpty:
			raise Exception
		index = self.findIndex(obj)
		if self._keys[index] == obj:
			if not self._subTrees[index].isEmpty:
				fmax = self._subTrees[index].max
				self._keys[index] = fmax
				self._subTrees[index].remove(fmax)
			elif not self._subTrees[index + 1].isEmpty:
				fmin = self._subTrees[index + 1].min
				self._keys[index] = fmin
				self._subTrees[index + 1].remove(fmin)
			else:
				i = index
				self._count -= 1
				while i < self.count:
					self._keys[i] = self._keys[i + 1]
					self._subTrees[i + 1] = self._subTrees[i + 2]
					i += 1
				self._keys[self.count] = None
				self._subTrees[self.count + 1] = None
		
		else:
			self._subTrees[index].remove(obj)
				
				
			
			
			
	def printTree(self):
		i = 0
		while i < self.keyLimit:
			print(str(self._keys[i]))
			i += 1
		i = 0
		print("|||")
		if not self.isEmpty:
			while i <= self.count:	
				self._subTrees[i].printTree()
				i += 1
			