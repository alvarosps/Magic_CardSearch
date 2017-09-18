#coding: utf-8

from MWayTree import MWayTree
from Array import Array
import abc

class BTree(MWayTree):
	
	def __init__(self, t):
		super(BTree, self).__init__(t)

		self._keys.setLength(self.keyLimit + 1)
		self._subTrees.setLength(self.keyLimit + 2)
		self._parent = None
		self._data = Array(self.keyLimit + 1)
		
	def getParent(self):
		return self._parent
		
	parent = property(
		fget = lambda self: self.getParent())
		
	# Copia uma arvore para outra.
	def copy(self, tree):
		self._keys = tree._keys
		self._subTrees = tree._subTrees
		self._count = tree.count
		self._t = tree.t 
		self._data = tree._data
		i = 0
		while i <= self.count:
			self._subTrees[i]._parent = self
			i += 1
	

	
	isEmpty = property(
		fget = lambda self: self.getIsEmpty())
	
	# Insere um elemento na árvore, usando a chave 'key'.
	def insert(self, key, data):
		if self.isEmpty:
			self._keys[0] = key
			self._subTrees[0] = BTree(self.t)
			self._subTrees[1] = BTree(self.t)
			self._count = 1
			self._data[0] = [data] 
		
		else:
			index = self.findIndex(key)
			if self._keys[index] == key:
				self._data[index].append(data)
			elif self.isLeaf:
				self.manualInsert(key, data)
				if self.count > self.keyLimit:
					self.split()
			else:
				self._subTrees[index].insert(key, data)
		
	# Faz um split na árvorem caso aconteça overflow.
	def split(self):
		middle = int(self.count / 2)
		left = BTree(self.t)
		right = BTree(self.t)
		left.attachLeftSideOf(self)
		right.attachRightSideOf(self)
		key = self._keys[middle]
		data = self._data[middle]
		
		if self.parent is None:
			self.purge()
			self._keys[0] = key
			self._data[0] = data 
			self._subTrees[0] = left
			self._subTrees[1] = right
			self._count = 1
			left._parent = self
			right._parent = self

		else:
			parent = self.parent
			parent.manualInsert(key, data) 
			index = parent.findIndex(key)
			self.copy(left)
			self._parent = parent
			right._parent = parent
			parent._subTrees[index] = self 
			parent._subTrees[index + 1] = right
	
			if parent.count > parent.keyLimit:
				self.parent.split()
				
	# Insere manualmente, fazendo shift nos elementos dos arrays..
	def manualInsert(self, key, data):
		if self.isEmpty:		
			self._keys[0] = key
			if isinstance(data, list): 
				self._data[0] = data 
			else: 
				self._data[0] = [data] 
			if self._subTrees[0] is None:
				self._subTrees[0] = BTree(self.t)
				
			
			self._subTrees[1] = BTree(self.t)
			self._subTrees[0]._parent = self
			self._subTrees[1]._parent = self
			self._count = 1
			
		else:
			index = self.findIndex(key)
			i = self.count
			while i > index:
				self._keys[i] = self._keys[i - 1]
				self._data[i] = self._data[i - 1] 
				self._subTrees[i + 1] = self._subTrees[i]
				i -= 1 
			
			self._keys[index] = key
			if isinstance(data, list): 
				self._data[index] = data 
			else: 
				self._data[index] = [data] 
			if self._subTrees[index + 1] is None:
				self._subTrees[index + 1] = BTree(self.t)
				self._subTrees[index + 1]._parent = self
			self._count += 1
			
		
	# Coloca a metade esquerda de uma árvore na outra.
	def attachLeftSideOf(self, tree):
		middle = int(tree.count / 2)
		i = self.count
		while i < middle:
			self.manualInsert(tree._keys[i], tree._data[i])
			self._subTrees[i] = tree._subTrees[i]
			self._subTrees[i]._parent = self
			i += 1
		self._subTrees[i] = tree._subTrees[i]
		self._subTrees[i]._parent = self
			
	# Coloca a metade direita de uma árvore na outra.
	def attachRightSideOf(self, tree):
		middle = int(tree.count / 2)
		i = middle + 1
		j = self.count
		while i < tree.count:
			self.manualInsert(tree._keys[i], tree._data[i]) 
			self._subTrees[j] = tree._subTrees[i]
			self._subTrees[j]._parent = self
			i += 1
			j += 1
		self._subTrees[j] = tree._subTrees[i]
		self._subTrees[j]._parent = self
	
		
	# Procura um elemento por uma chave.
	def find(self, key):
		if self is None:
			print("Not found.")
		else:
			i = 0
			while i < len(self._keys):
				if self._keys[i] == key:
					return self._data[i]
				i += 1
				
			index = self.findIndex(key)
			if self._subTrees[index] is None:
				print("Not found.")
			else:
				return self._subTrees[index].find(key)
			
			

	# Reseta a árvore para as condições iniciais.
	def purge(self):
		self._count = 0
		self._data.purge()
		self._keys.purge()
		self._subTrees.purge()



