#codign: utf-8

from abc import *
from Array import Array

class Objeto(object):
    def __init__(self):
        super(Objeto, self).__init__()
    def __cmp__(self, obj):
        if isinstance(self, obj.__class__):
            return self._compareTo(obj)
        elif isinstance(obj, self.__class__):
            return -obj._compareTo(self)
        else:
            return cmp(self.__class__.__name__, obj.__class__.__name__)

    @abstractmethod
    def _compareTo(self, obj): pass



class Sorter(Objeto):
    def __init__(self, array):
        super(Sorter, self).__init__()
        self._N = len(array)        #Tamanho do vetor a ser ordenado
        self._V = array                #Vetor a ser ordenado
        self._comp = 0                 #Numero de comparacoes feitas para ordenar o vetor
        self._troc = 0                 #Numero de trocas feitas para ordenar o vetor

    @abstractmethod
    def _sort(self): pass

    def sort(self):
        assert isinstance(self._V, Array)
        
        self._sort(0, self._N - 1)
        

    def troca(self, i, j):
        tmp = self._V[i]
        self._V[i] = self._V[j]
        self._V[j] = tmp
        self._troc += 1
        
class QuickSorter(Sorter):
    def __init__(self, array):
        super(QuickSorter, self).__init__(array)
    
    def _sort(self, esquerda, direita):
        pivo = self._V[ int((esquerda+direita)/2) ]
        i = esquerda
        j = direita
        
        while i <= j:
            while self._V[i] < pivo:
                i += 1
            while self._V[j] > pivo:
                j -= 1
            if i <= j:
                self.troca(i, j)
                i += 1
                j -= 1
        if esquerda < j:
            self._sort(esquerda, j)
        if i < direita:
            self._sort(i, direita)