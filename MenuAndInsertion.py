#coding: utf-8

import json
from pprint import pprint
from TrieTree import TrieTree
from BTree import BTree
import re
import os
import pickle
from Quicksort import *
from Array import *

"""
 Como pesquisar:
 parametros possiveis: name=, type=, text=, manacost=, power=, toughness=, cmc=
 
 Exemplo: name=goblin text=deals
 Vai pesquisar por nomes que contem goblin e textos que contel deals.
 
 Exemplo: color=blue color=red cmc=4
 Procura por cartas com cores azul e vermelhas, com cmc de 4.
 
 Depois de pesquisar, se escrever somente view=, seguido de um indice, ele mostra tal carta na tela
 

"""

# Arvores.
name = TrieTree(25)
type = TrieTree(25)
text = TrieTree(25)
colors = TrieTree(25)
manacost = TrieTree(25)
power = BTree(4)
toughness = BTree(4)
cmc = BTree(4)


def read_cards_from_origin():
    with open("AllCards.json", 'r') as json_file:
        json_data = json.load(json_file)
        for key in json_data.keys():
           
            # Insere os nomes.
            name.insert(json_data[key]["name"], key)
         
            # Insere os tipos na arvore de tipos.
            if "type" in json_data[key]:
                # Se houver caracteres estranhos, da erro; entao tem que tirar.
                try:
                    cardType = json_data[key]["type"].replace('Ã¢', '')
                    cardType = cardType.replace('â‚¬', '')
                    cardType = cardType.replace('â€�', '')
                except:
                    cardType = json_data[key]["type"]
                type.insert(cardType, key)
            # Insere textos.
            if "text" in json_data[key]:
                text.insert(json_data[key]["text"], key)
            # Insere poder.
            if "power" in json_data[key]:
                new = json_data[key]["power"]
                # Retira os caracteres que nao sao numeros, substituindo por 0.
                new = re.sub("[^0-9]", "0", new)
                power.insert(int(new), key)
            # Insere defesa.
            if "toughness" in json_data[key]:
                # Retira os caracteres que nao sao numeros, substituindo por 0.
                new = json_data[key]["toughness"]
                new = re.sub("[^0-9]", "0", new)
                toughness.insert(int(new), key)
            # Insere cmc.
            if "cmc" in json_data[key]:
                cmc.insert(int(json_data[key]["cmc"]), key)   
            # Insere cores.
            if "colors" in json_data[key]:
                for color in json_data[key]["colors"]:
                    colors.insert(color, key)
            # Insere custo de mana.
            if "manaCost" in json_data[key]:
                # Retira chaves que existem nas strings.
                new = json_data[key]["manaCost"].replace("{", "")
                new = new.replace("}", "")
                manacost.insert(new, key)
        
    return [name, type, text, colors, manacost, power, toughness, cmc]
      
def write_cards_file(list_cards):
    #Escreve as estruturas em arquivos bin�rios
    with open("estruturas.pkl", "wb") as arq:
        pickle.dump(list_cards, arq, pickle.HIGHEST_PROTOCOL)
    del list_cards  #Apaga para nao ficar na memoria as estruturas

def read_cards_file():
    #Le o arquivo com as estruturas para usar nas pesquisas
    with open("estruturas.pkl", "rb") as arq:
        list_trees = pickle.load(arq)
    return list_trees
# Procura nas arvores
def searchCard(searchParameters, trees):
    wordList = searchParameters.split(' ')
    cards = []
    
    name = trees[0]
    type = trees[1]
    text = trees[2]
    colors = trees[3]
    manacost = trees[4]
    power = trees[5]
    toughness = trees[6]
    cmc = trees[7]
    
    for param in wordList:
        # Pesquisa o paramentro na arvore dos nomes.
        if "name=" in param:
            param = param.replace("name=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, name.find(param)))
            else:
                cards = name.find(param)
                
        # Pesquisa o parametro na arvore dos textos.
        if "text=" in param:
            param = param.replace("text=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, text.find(param)))
            else:
                cards = text.find(param)
                
        # Pesquisa o parametro na arvore dos tipos.
        if "type=" in param:
            param = param.replace("type=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, type.find(param)))
            else:
                cards = type.find(param)
                
        # Pesquisa o parametro na arvore dos poderes.
        if "power=" in param:
            param = param.replace("power=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, power.find(int(param))))
            else:
                cards = power.find(int(param))
                
        # Pesquisa o parametro na arvore da defesa.
        if "toughness=" in param:
            param = param.replace("toughness=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, toughness.find(int(param))))
            else:
                cards = toughness.find(int(param))
                
        # Pesquisa o parametro na arvore do custo de mana covertido (cmc).
        if "cmc=" in param:
            param = param.replace("cmc=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, cmc.find(int(param))))
            else:
                cards = cmc.find(int(param))
                
        # Pesquisa o parametro na arvore das cores.
        if "color=" in param:
            param = param.replace("color=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, colors.find(param)))
            else:
                cards = colors.find(param)
                
        # Pesquisa o parametro na arvore dos custos de mana.
        if "manacost=" in param:
            param = param.replace("manacost=", "")
            if len(cards) != 0:
                cards = list(filter(set(cards).__contains__, manacost.find(param)))
            else:
                cards = manacost.find(param)
    
    
    return cards


# Mostra a carda desejada.
def viewCard(cardList, index):
    if index < len(cardList):
        print(json_data[cardList[index]])


def menu():
    loop = True
    print("Bem vindo ao sistema de busca sobre Magic!")
    while loop == True:
        print("\nOpcoes:")
        print("0 - Ler arquivo de cartas e armazenar no sistema.")
        print("1 - Pesquisa de cartas.")
        print("9 - Encerrar programa.")
        op = int(input("\nDigite o numero referente a opcao escolhida: "))
        
        if op == 0:
            try:
                cards = read_cards_from_origin()
                write_cards_file(cards)
                print("Dados lidos e armazenados com sucesso!")
                cont = input("Pressione ENTER para continuar.")
                os.system("cls")
            except Exception as error:
                print("Ocorreu um erro: ", error)
                cont = input("Pressione ENTER para continuar.")
                os.system("cls")
        elif op == 1:
            try:
                trees_list = read_cards_file()
            
                ans = True
                cards = []
                while ans:                    
                    ans = input("Procure por uma(s) carta(s)! Digite: ")
                    sort = input("Deseja as cartas em ordem 'normal' ou inversa(digite 'inversa') sem as aspas: ")
                    if sort != "normal" and sort != "inversa":
                        print("Voce nao escolheu uma ordem valida, por padrao, sera imprimido em ordem normal.")
                    if "view=" in ans:
                        viewCard(cards, int(ans.replace("view=", "")))
                    else:
                        print()
                        cards = searchCard(ans, trees_list)
                        
                        cards_Array = Array(len(cards))
                        for i in range(len(cards)):
                            cards_Array[i] = cards[i]
                        cards_quicksorter = QuickSorter(cards_Array)
                        cards_quicksorter.sort()
                        cards_sorted = []
                        
                        if sort == "inversa":
                            for i in range(len(cards_quicksorter._V) - 1, -1, -1):
                                cards_sorted.append(cards_quicksorter._V[i])
                        else:
                            for i in range(len(cards_quicksorter._V)):
                                cards_sorted.append(cards_quicksorter._V[i])
                        
                        
                        del cards
                        del cards_Array
                        del cards_quicksorter
                            
                        
                        i = 0
                  
                        for j in cards_sorted:
                            print("[", i,"]: ", j)
                            i += 1
                        del cards_sorted
                    try:
                        continuar = int(input("\nDigite 9 para encerrar. Qualquer outro numero para continuar"))
                        if continuar == 9:
                            ans = False
                    except ValueError:
                        print("Voce digitou um numero invalido. a busca sera continuada")
                cont = input("Voce encerrou a busca. Pressione ENTER para continuar")
                os.system("cls")
            except FileNotFoundError:
                print("Voce ainda nao criou o arquivo, o programa vai voltar ao menu inicial")
                cont = input("Pressione ENTER para continuar")
                os.system("cls")
        elif op == 9:
            print("\nPrograma encerrado.")
            loop = False

