# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 30/11/2017
# Compiladores - Ciência Da Computação
# PyGraph.py
# -----------------------------------------------------------------------------
import sys

class PyVertice:
    def __init__(self, name, valor=None):
        self.name = name
        self.valor = valor

    def __str__(self):
        return str(self.name)

class PyAresta:
    def __init__(self, vertice, symbol):
        self.vertice = vertice
        self.symbol = symbol

    def __str__(self):
        return str(str(self.vertice) + ' - ' + self.symbol )

class PyGraph:
    def __init__(self, digrafo=0):
        self.tempo = 0
        self.digrafo = digrafo
        self.grafo = []
        self.vetorDistancia = []
        self.adj = []

   #função para inserir dois nos e suas arestas ou uma aresta somente
    def inserirNo(self, vertice):
        #caso venha somente um nó (ele não se liga a nenhum outro)
        if(1 if self.verificaNomeVertice(vertice) == None else 0):
            self.grafo.append(vertice)
            self.adj.append([vertice,[]])

    #verifica se existe um vertice com o nome ja no grafo
    def verificaNomeVertice(self, vertice):
        aux = None
        for vert in self.grafo:
            if(vert.name == vertice.name):
                aux = vert
        return aux

    #verifica se existe um vertice com o nome ja no grafo
    def retornVertByName(self, name):
        aux = None
        for vert in self.grafo:
            if(vert.name == name):
                aux = vert
        return aux

    #função para inserir uma nova aresta
    def inserirAdj(self, vertice, vertice2, symbol):
        vertice = self.verificaNomeVertice(vertice)
        vertice2 = self.verificaNomeVertice(vertice2)
        index = self.grafo.index(vertice)
        self.adj[index][1].append(PyAresta(vertice2,symbol))

        if self.digrafo == 0:
            index2 = self.grafo.index(vertice2)
            self.adj[index2][1].append(vertice)

    #retorna a lista de adjascencia de um nó bidirecional
    def getAdjacentes(self, no, Letter):

        adjs = []
        adjsByLetter = []

        for linha in self.adj:
            if(linha[0].name == no.name):
                adjs = linha[1]
        
        for adj in adjs:
            if(adj.symbol == Letter):
                adjsByLetter.append(adj)

        return adjsByLetter

    def printGrafo(self):
        print("\nGrafo: ")
        sys.stdout.write("[")
        for vertice in self.grafo:
            sys.stdout.write("- "+str(vertice)+" ")
        print("]")

    def printAdjacencia(self):
        print("\nAdjascencia:")
        for vertice in self.adj:
            sys.stdout.write(str(vertice[0])+" -> ")
            for vertice2 in vertice[1]:
                sys.stdout.write(str(vertice2))
                if(not vertice[1].index(vertice2) == len(vertice[1])-1):
                    sys.stdout.write(" | ")
            print()
