#coding: utf-8

from SearchTree import SearchTree
from Array import Array

class TrieTree(SearchTree):
	
	def __init__(self, maxSubTrees):
		super(TrieTree, self).__init__()
		self._key = None
		self._data = []
		self._subTrees = Array(maxSubTrees + 65)
		self._maxSubTrees = maxSubTrees + 65
	
	
	def getData(self):
		return self._data
		
	data = property(
		fget = lambda self: self.getData())
	
	def getKey(self):
		return self._key
		
	def setKey(self, value):
		self._key = value
		
	key = property(
		fget = lambda self: self.getKey(),
		fset = lambda self, value: self.setKey(value))
		
	def getMaxSubTrees(self):
		return self._maxSubTrees
		
	maxSubTrees = property(
		fget = lambda self: self.getMaxSubTrees())
		
	def getIsEmpty(self):
		return self.key is None
		
	isEmpty = property(
		fget = lambda self: self.getIsEmpty())
		
	def getOrder(self, char):
		index = ord(char)
		if index > 122:
			index = ord('e')
		if index >= ord('a'):
			return index - 97
		else:
			return ord(char) - 6
			# - 32
	
	# Funcao de busca:	
	#
	# key : string chave
	# level : argumento que monitora o nivel do nodo atual. Sempre comeca no zero.
	def find(self, key, level=0):
		lowerKey = key.lower()
		lowerKey = lowerKey.replace(",", "")
		if self._key == lowerKey:
			return self._data
		elif level == len(key):
			print("not found", key)
			return []
		else:
			index = self.getOrder(lowerKey[level])
			if self._subTrees[index] == None:
				print("Not found.", key)
				return []
			else:
				return self._subTrees[index].find(lowerKey, level + 1)


	# Funcao de insercao
	#
	# key : string chave
	# data : informacao que sera armazenada no nodo de cada palavra da frase.
	def insert(self, key, data):
		lowerKey = key.lower()
		lowerKey = lowerKey.replace(",", "")
	
		wordList = lowerKey.split(' ')
		i = 0
		while i < len(wordList):
			if len(wordList[i]) > 0:
				self.insertWord(wordList[i], data, -1)
			i += 1
			
	# Funcao auxiliar de insert()
	#
	# key : string chave
	# data : informacao que sera armazenada no nodo
	# level : argumento que monitora o nivel do nodo atual
	def insertWord(self, key, data, level):
		if len(key) == level:
			self._key = key
			self._data.append(data) 
		else:
			if level == -1:
				level = 0
			
	
			index = self.getOrder(key[level])
			
			
			
			if self._subTrees[index] is None:
				new = TrieTree(self.maxSubTrees)
				self._subTrees[index] = new
				new.insertWord(key, data, level + 1)
			else:
				self._subTrees[index].insertWord(key, data, level + 1)
		

		
	def listAll(self, strList):
		if not self._key is None:
			strList.append(self._key)
		for sub in self._subTrees:
			if not sub is None:
				strList = sub.listAll(strList)
			
		return strList
		
		
		
		
		
		
