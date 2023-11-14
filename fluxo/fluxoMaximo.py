import auxiliar as a
        
graph = open('graph.txt')
for line in graph.readlines():
    line = line.split()
    inicio = line[0]
    fim = line[1]
    fluxo = line[2]
    a.criarVertice(inicio)
    a.criarVertice(fim)
    a.adicionarAresta (inicio, fim, fluxo)

fluxo = a.FordFulkerson(a.G, 'S', 'T')
print (f'- o fluxo maximo eh {fluxo}')
print ('---------- FLUXO ELEMENTAR EM CADA ARESTA ----------')
vertices = a.G.keys()
for v in vertices:
    adj = a.G[v].keys()
    for u in adj:
        print (f' {v}-{u}: {a.G[v][u]} ||', end = '')
