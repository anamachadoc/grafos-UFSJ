adjacencia = {}

def adicionarVertice(v):
    if v not in adjacencia.keys():
        adjacencia[v] ={
                'adj': [],
                'fluxo': []
            }
        
def adicionarAdjacencia(v, u, fluxo):
    adjacencia[v]["adj"].append(u)
    adjacencia[v]["fluxo"].append(fluxo)
    adjacencia[u]["adj"].append(v)
    adjacencia[u]["fluxo"].append(0)
     
# reading an directed graph
G = open('graph.txt')
for line in G.readlines():
    line = line.split()
    inicio = line[0]
    fim = line[1]
    fluxo = line[2]
    adicionarVertice(inicio)
    adicionarVertice(fim)
    adicionarAdjacencia (inicio, fim, fluxo)

print(adjacencia)

