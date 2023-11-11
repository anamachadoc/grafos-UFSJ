import sys

G = {}
fluxoElementar = {}

def criarVertice(v):
    if v not in G.keys():
        G[v] ={
                'adj': [],
                'fluxo': [], # o que pode passar
                'flag': 0 # pode passar fluxo por ali - 1 nao pode
            }
        
def adicionarFluxo(u, v, valor):
    aresta = v + u
    if aresta not in fluxoElementar.keys():
        fluxoElementar[aresta] = valor
    else:
        fluxoElementar[aresta] = fluxoElementar[aresta] + valor
        
def adicionarAresta(v, u, fluxo):
    G[v]["adj"].append(u)
    G[v]["fluxo"].append(fluxo)
     
# reading an directed graph
graph = open('graph.txt')
for line in graph.readlines():
    line = line.split()
    inicio = line[0]
    fim = line[1]
    fluxo = line[2]
    criarVertice(inicio)
    criarVertice(fim)
    adicionarAresta (inicio, fim, fluxo)
    
# ----------------------------------------------------------------
    
def definirCaminho(v, caminho, menor):
    if (v != 'T'):
        novoVertice = G[v]['fluxo'].index(max(G['S']['fluxo'])) # achar onde passa mais fluxo
        if G[v]['fluxo'][novoVertice] < menor:
            menor = G[v]['fluxo'][novoVertice]
        caminho.append(G[v]['adj'][novoVertice])
        definirCaminho (G[v]['adj'][novoVertice], caminho, menor)
    return caminho 

def passarFluxo(caminho, valorFluxo):
    while (len(caminho) != 1):
        ultimo = caminho[len(caminho) - 1] 
        anterior = caminho[len(caminho) - 2]
        adicionarFluxo (ultimo, anterior, valorFluxo)
        pos = G[anterior]['adj'].index(ultimo)
        G[anterior]['fluxo'][pos] = G[anterior]['fluxo'][pos] - valorFluxo
        if G[anterior]['fluxo'][pos] == 0: # aresta saturada
            
        caminho.remove(ultimo)
        
# ----------------------------------------------------------------
 
# algorithm
caminho = []
caminho.append('S')
while (G['S']['flag'] == 0): # enquanto for possivel passar fluxo por S
    menor = sys.maxsize
    caminho = definirCaminho ('S', caminho, menor)
    passarFluxo (caminho, menor)
print(G)
    
print(G)

