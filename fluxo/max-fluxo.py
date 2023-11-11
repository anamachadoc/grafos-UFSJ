import funcoes as f

# reading an directed graph
graph = open('graph.txt')
for line in graph.readlines():
    line = line.split()
    inicio = line[0]
    fim = line[1]
    fluxo = line[2]
    f.criarVertice(inicio)
    f.criarVertice(fim)
    f.adicionarAresta (inicio, fim, fluxo)
# algorithm
caminho = ['S'] # caminho com a unica origem definida
while (f.G['S']['flag'] == 1):
    f.escolherCaminho ('S', caminho)
    u = caminho[len(caminho)-1] 
    if (u == 'T'): # consigo chegar ate T
        passarFluxo(caminho)
    else:
        f.G[u]['flag'] = 0 # vertice saturado
        
    f.G['S']['flag'] = 0
print (caminho)