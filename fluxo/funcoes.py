G = {}

def criarVertice(v):
    if v not in G.keys():
        G[v] ={
            'flag': 1
        }
        
def adicionarAresta(v, u, fluxo):
    G[v][u] = fluxo
    G[u][v] = 0
    
def escolherCaminho (v, caminho):
    Vertices = list(G[v].keys()) # sao os adjacentes, fora flag 
    i = 1
    u = Vertices[i]
    while (G[v][u] == 0 and i < len(Vertices)):
        i = i + 1
        u = Vertices[i]
    caminho.append(u)
    if (G[v][u] == 0 or u == 'T'): # nao tem mais caminho
        print ('caminho')
        return 
    escolherCaminho (u, caminho)
        
def passarFluxo (caminho, valorFluxo):
    while (len(caminho) != 1):
        u = caminho[len(caminho) - 1] 
        v = caminho[len(caminho) - 2]
        G[v][u] = G[v][u] - valorFluxo
        G[u][v] = G[u][v] + valorFluxo
        caminho.remove(u)