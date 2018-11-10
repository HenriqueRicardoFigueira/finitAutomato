from PyGraph import PyGraph, PyAresta, PyVertice

if __name__ == '__main__':
    PyGraph = PyGraph()

    PyGraph.digrafo = 1

    #inserção
    q0 = PyVertice("q0")
    PyGraph.inserirNo(q0)
    q1 = PyVertice("q1")
    PyGraph.inserirNo(q1)
    q2 = PyVertice("q2")
    PyGraph.inserirNo(q2)

    
    #insere adjascencia
    PyGraph.inserirAdj(q0,q0,"a")
    PyGraph.inserirAdj(q0,q1,"b")
    PyGraph.inserirAdj(q1,q2,"b")
    PyGraph.inserirAdj(q2,q1,"b")

    #remoção
    #PyGraph.removerNo(vertice3)
    
    #recebe os nos do Grafo
    print("\nNos:")
    nos = PyGraph.getNos()
    for i in nos:
        print(i)
    
    PyGraph.printAdjacencia()

    #recebe a lista de adj de um Grafo
    print("\nADJ de "+str(PyGraph.grafo[0])+":")
    nos = PyGraph.getAdjacentes(PyGraph.grafo[0])
    for i in nos:
        print(i)