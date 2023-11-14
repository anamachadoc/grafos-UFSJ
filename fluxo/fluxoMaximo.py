import auxiliar as a
        
# leitura do arquivo de entrada
graph = open('graph.txt')
for line in graph.readlines():
    line = line.split()
    inicio = line[0]
    fim = line[1]
    fluxo = line[2]
    a.criarVertice(inicio)
    a.criarVertice(fim)
    a.adicionarAresta (inicio, fim, fluxo)
    
def FordFulkerson(G, origem, fim):
    # antecessor eh utilizado para saber por onde chegou-se ate determinado vertice 
    antecessor = {}
    a.inserirChaves (antecessor, G)
    fluxoMaximo = 0
    while a.BFS(G, origem, fim, antecessor):
        aux = fim
        fluxoCaminho = G[antecessor[aux]][aux]
        # encontrando o menor valor de fluxo naquele caminho = o fluxo que pode passar
        while aux != origem: 
            fluxoCaminho = min(fluxoCaminho, G[antecessor[aux]][aux])
            aux = antecessor[aux]
        # somando ao valor de fluxo maximo
        fluxoMaximo += fluxoCaminho
        v = fim
        # atualizando valores no grafo de folgas
        while v != origem:
            u = antecessor[v]
            a.passarFluxo (G, v, u, fluxoCaminho)
            a.passarFluxo (G, u, v, -fluxoCaminho)
            v = antecessor[v]      
    return fluxoMaximo

fluxo = FordFulkerson(a.G, 'S', 'T')

print (f'\nO fluxo maximo eh {fluxo}\n')
print ('---------- FLUXO ELEMENTAR EM CADA ARESTA ----------')
vertices = a.G.keys()
for v in vertices:
    adj = a.G[v].keys()
    for u in adj:
        print (f'{v}-{u}: {a.G[v][u]}')
