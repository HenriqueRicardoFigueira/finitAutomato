from PyGraph import PyGraph, PyAresta, PyVertice

class AFD:
    def __init__(self):
        self.FinalStates = []
        self.InitialState = None
        self.InitialWord = ['a','b']
        self.SymbolNull = '#'
        self.State = None

    def isEnd(self):
        if(len(self.State.valor) == 0 and self.State not in self.FinalStates):
            print("rejeitado")
            print(1)
            exit(1)

        return bool(self.State in self.FinalStates and len(self.State.valor) == 0)

    def caminha(self, vertInicial, pygraph):
        adjs = pygraph.getAdjacentes(vertInicial, vertInicial.valor[0])

        if(len(adjs) == 1):
            adj = adjs[0]
            if(adj.symbol == vertInicial.valor[0]):
                if(vertInicial.valor[0] != self.SymbolNull):
                    adj.vertice.valor = vertInicial.valor[1:]
                    self.State = adj.vertice



    def __main__(self):
        pygraph = PyGraph()
        
        pygraph.digrafo = 1

        #inserção
        q0 = PyVertice("q0")
        pygraph.inserirNo(q0)
        q1 = PyVertice("q1")
        pygraph.inserirNo(q1)
        q2 = PyVertice("q2")
        pygraph.inserirNo(q2)

        self.FinalStates.append(q1)
        self.InitialState = q0
        q0.valor = self.InitialWord
        self.State = q0
        
        #insere adjascencia
        pygraph.inserirAdj(q0,q0,"a")
        pygraph.inserirAdj(q0,q1,"b")
        pygraph.inserirAdj(q1,q2,"b")
        pygraph.inserirAdj(q2,q1,"b")

        #remoção
        #PyGraph.removerNo(vertice3)
        
        #recebe os nos do Grafo
        print("\nNos:")
        nos = pygraph.getNos()
        for i in nos:
            print(i)
        
        pygraph.printAdjacencia()


        #executa
        while(not self.isEnd()):
            self.caminha(self.State,pygraph)
            pass


        #fim
        print(0)
        exit(0)

AFD().__main__()