#coding: utf-8

class Array(object):

	# __init__(self, length=0, baseIndex=0)
	# Complexidade: O(n) 
	#
	# Cria uma lista vazia (com 'None's) de um certo tamanho 'length', ###
	#
	# length : tamanho do array.
	# baseIndex : primeiro index do array.
	def __init__(self, length=0, baseIndex=0):
		assert length > 0
		self._data = [None for i in range(length)]
		self._baseIndex = baseIndex
		
	# __copy__(self)
	# Complexidade: O(n)
	#
	# Retorna o conteudo do array da instancia atual.
	def __copy__(self):
		result = Array(len(self._data))
		for i, datum in enumerate(self._data):
			result._data[i] = datum
		result._baseIndex = self._baseIndex
		return result
	
	# getOffset(self, index)
	# Complexidade: O(1).
	#
	# Retorna o index correto, fazendo a diferenca entre o index
	# dado e indice base.
	#
	# index : indíce a partir do qual o offset será calculado.
	def getOffset(self, index):
		offset = index - self._baseIndex
		if offset < 0 or offset > len(self._data):
			raise IndexError
		return offset
		
		
	# __getitem__(self, index)
	# Complexidade: O(1).
	#
	# Retorna o valor que está em um certo index.
	#
	# index : índice onde o valor está guardado.
	def __getitem__(self, index):
		return self._data[self.getOffset(index)]
		
	# __setitem__(self, index, value)
	# Complexidade: O(1).
	#
	# Define o valor do índice dado.
	#
	# index : indíce no qual o valor será mudado.
	def __setitem__(self, index, value):
		self._data[self.getOffset(index)] = value
		
	# getData(self)
	# Complexidade: O(1).
	def getData(self):
		return self._data
		
	data = property(
		fget = lambda self: self.getData())
		
	# getBaseIndex(self)
	# Complexidade: O(1).
	def getBaseIndex(self):
		return self._baseIndex
		
	# setBaseIndex(self, value)
	# Complexidade: O(1).
	def setBaseIndex(self, value):
		self._baseIndex = value
		
	baseIndex = property(
		fget = lambda self: self.getBaseIndex(),
		fset = lambda self, value: self.setBaseIndex(value))
		
	# __len__(self)
	# Complexidade: O(1)
	def __len__(self):
		return len(self._data)
		
	# setLength(self, value)
	# Complexidade: O(min(self.len(self._data), value)) (O(m))
	#
	# Modifica o tamanho do array.
	#
	# value : tamanho novo do array.
	def setLength(self, value):
		if len(self._data) != value:
			newData = [None for i in range(value)]
			m = min(len(self._data), value)
			for i in range(m):
				newData[i] = self._data[i]
			self._data = newData
			
			
	def purge(self):
		i = self.baseIndex
		while i < len(self.data):
			self._data[i] = None
			i += 1
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
