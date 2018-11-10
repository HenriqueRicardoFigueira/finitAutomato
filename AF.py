from PyGraph import PyGraph, PyAresta, PyVertice
from Start import Start
import sys

class AFD:
    def __init__(self):
        self.start = Start(sys.argv)
        self.pygraph = PyGraph()
        self.pygraph.digrafo = 1

        #inserção estados
        for state in self.start.getStates():
            var = PyVertice(state)
            self.pygraph.inserirNo(var)

        #inserção transições dos estados
        for transition in self.start.getTrans():
            ini = self.pygraph.retornVertByName(transition[0])
            final = self.pygraph.retornVertByName(transition[2])
            self.pygraph.inserirAdj(ini,final,transition[1])


        #inserção dos estados finais
        self.FinalStates = []
        for final in self.start.getFinal():
            self.FinalStates.append(self.pygraph.retornVertByName(final))

        #demais inserções (estado inicial, palavra inicial, simbolo branco, estado final)
        self.InitialState = self.pygraph.retornVertByName(self.start.getInitial())
        self.InitialWord = list(sys.argv[2])
        self.InitialState.valor = self.InitialWord
        self.SymbolNull = self.start.getSimbol()
        self.States = []
        self.States.append(self.pygraph.retornVertByName(self.start.getInitial()))

    def getCurrentState(self, state):
        sys.stdout.write("Estados Finais: ")
        for final in self.FinalStates:
            sys.stdout.write(str(final))
            sys.stdout.write(' ')
        print("\nEstado: "+str(state.name))
        print("Palavra: "+str(state.valor))
        for i in self.pygraph.retAdjacentes(state):
            print("Transições Possíveis: "+str(i))
        print("-------------------------------------")

    def isEnd(self):
        remocoes = []

        for state in self.States:
            if(len(state.valor) != 0  and len(self.pygraph.getAdjacentes(state, state.valor[0])) == 0):
                if(len(self.States) > 1 ):
                    remocoes.append(state)
                else:
                    print("Descrição Instantânea: \n_________________________________________")
                    self.getCurrentState(state)
                    print("Código de sáida: 1")
                    exit(1)

            elif(len(state.valor) == 0 and self.pygraph.retornVertByName(state.name) not in self.FinalStates):
                if(len(self.States) > 1 ):
                    remocoes.append(state)
                else:
                    print("Descrição Instantânea: \n_________________________________________")
                    self.getCurrentState(state)
                    print("Código de sáida: 1")
                    exit(1)
            
            if(self.pygraph.retornVertByName(state.name) in self.FinalStates and len(state.valor) == 0):
                print("Descrição Instantânea: \n_________________________________________")
                self.getCurrentState(state)
                return True

        if(len(self.States) > len(remocoes)):
            for i in remocoes:
                self.States.remove(i)
            
        else:
            print("Descrição Instantânea: \n_________________________________________")
            for i in remocoes:
                self.getCurrentState(i)
            print("Código de sáida: 1")
            exit(1)

        return False

    def caminha(self):

        newStates = []
        
        for vertInicial in self.States:
            adjs = self.pygraph.getAdjacentes(vertInicial, vertInicial.valor[0])

            if(len(adjs) == 1):
                adj = adjs[0]
                if(adj.symbol == vertInicial.valor[0]):
                    if(vertInicial.valor[0] != self.SymbolNull):
                        newState = PyVertice(adj.vertice.name, vertInicial.valor[1:])
                        newStates.append([newState,vertInicial])
                    else:
                        newState = PyVertice(adj.vertice.name, vertInicial.valor)
                        newStates.append([newState,vertInicial])
            
            if(len(adjs) > 1):
                for adj in adjs:
                    if(adj.symbol == vertInicial.valor[0]):
                        if(adj.symbol != self.SymbolNull):
                            newState = PyVertice(adj.vertice.name, vertInicial.valor[1:])
                            newStates.append([newState,vertInicial])
                        else:
                            newState = PyVertice(adj.vertice.name, vertInicial.valor)
                            newStates.append([newState,vertInicial])

                            
        for state in newStates:
            try:
                self.States.append(state[0])
                self.States.remove(state[1])
            except:
                pass
                        
                        
    def __main__(self):

        #executa
        while(not self.isEnd()):
            self.caminha()
            pass

        #fim
        print("Código de sáida: 0")
        exit(0)

AFD().__main__()