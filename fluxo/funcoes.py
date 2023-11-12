G = {}

def criarVertice(v):
    if v not in G.keys():
        G[v] ={
            'flag': 1
        }
        
def adicionarAresta(v, u, fluxo):
    G[v][u] = int(fluxo)
    G[u][v] = 0
    
def passarFluxo(caminho, valorFluxo):
    while (len(caminho) != 1):
        u = caminho[len(caminho) - 1] 
        v = caminho[len(caminho) - 2]
        G[v][u] = G[v][u] - valorFluxo
        G[u][v] = G[u][v] + valorFluxo
        caminho.remove(u)
    print ('grafo depois de passar o fluxo:')
    print(G)
        
def voltarAtras (v, i, Vertices, caminho, valorFluxo):
    if (i + 1 < len(Vertices)): # ainda tem  mais vertices que pode olhar
            verificarVertice (Vertices, i+1, v, caminho, valorFluxo)
    else:
        print(f'v:{v} saturado')
        G[v]['flag'] = 0 # saturo a aresta que me trouxe ate ali
        return 

def verificarVertice (Vertices, i, v, caminho, valorFluxo):
    u = Vertices[i]
    print (f'verificando u:{u}')
    print (f'i:{i}')
    print (f'v:{v} - u:{u}')
    print (G[v][u])
    if (G[v][u] == 0):
        print (f'volta atras pq nao pode passar por u:{u} pq o fluxo ali eh zero') 
        voltarAtras (v, i, Vertices, caminho, valorFluxo)
    elif (G[u]['flag'] == 0): # nao passa em aresta saturada 
        print (f'volta pq u:{u} ja esta saturado')
        voltarAtras (v, i, Vertices, caminho, valorFluxo)
    elif (len(caminho) > 2 and u == caminho[len(caminho)-2]): # nao volta pra tras
        # PROBLEMA AQUI
        print('tava voltando pra tras')
        voltarAtras (v, i, Vertices, caminho, valorFluxo)
    else:
        print(f'adicionando:{u}')
        caminho.append(u)
        print('caminho ate agora:',caminho)
        valorFluxo.append(G[v][u])
    
def escolherCaminho (v, caminho, valorFluxo):
    Vertices = list(G[v].keys()) # sao os adjacentes, fora flag 
    print(f'Vertices:{Vertices}')
    i = 1
    verificarVertice(Vertices, i, v, caminho, valorFluxo)
    u = caminho[len(caminho)-1]
    if (u != 'T' and G[u]['flag'] == 1): # tem mais caminho
        print (f'seguindo para u: {u}')
        escolherCaminho (u, caminho, valorFluxo)
    print (f'caminho definido: {caminho}')
    return
        
        
        