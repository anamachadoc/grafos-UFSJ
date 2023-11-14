G = {} # G eh o grafo de folgas

# todo vertice possui um dicionario com seus adjacentes e os valores das arestas que os ligam
def criarVertice(v): 
    if v not in G.keys():
        G[v] ={}

def adicionarAresta(v, u, fluxo):
    G[v][u] = int(fluxo)
    G[u][v] = int(0)
    
def zerarVisitados (visitados, G):
    v = list(G.keys())
    for vertice in v:
        visitados[vertice] = False
       
def inserirChaves (anteriores, G):
    v = list(G.keys())
    for vertice in v:
        anteriores[vertice] = 'None'
        
def passarFluxo (G, inicio, fim, valorFluxo):
    G[inicio][fim] += valorFluxo
    
# busca em largura para determinar os caminhos
def BFS(G, s, t, anteriores):
    visitados = {}
    zerarVisitados (visitados, G) # a cada novo caminho, todos os vertices devem estar com a chave visitado como False
    fifo = [] # fila que auxilia na montagem do caminho
    fifo.append(s) # primeiro elemento eh a origem
    visitados[s] = True
 
    while fifo:
        u = fifo.pop(0)
        adj = list(G[u].keys())
        for v in adj: # olha os adjacentes do vertice removido - primeiro da fila
            # adiciona na fila os possiveis = nao visitado e possivel de passar fluxo
            if visitados[v] is False and G[u][v] > 0:
                fifo.append(v)
                visitados[v] = True
                anteriores[v] = u # define o anterior ao elemento adicionado
    # se chegou ate T entao retorna o caminho - se nao quer dizer que todos os caminhos possiveis ja foram olhados
    return True if visitados[t] else False

def FordFulkerson(G, origem, fim):
    # anteriores eh utilizado para saber por onde chegou-se ate determinado vertice - dicionario com todos os vertices de G
    anteriores = {}
    inserirChaves (anteriores, G)
    fluxoMaximo = 0
    while BFS(G, origem, fim, anteriores):
        aux = fim
        fluxoCaminho = G[anteriores[aux]][aux]

        # encontrando o menor valor de fluxo naquele caminho = o fluxo que pode passar
        while aux != origem: 
            fluxoCaminho = min(fluxoCaminho, G[anteriores[aux]][aux])
            aux = anteriores[aux]
 
        # somando ao valor de fluxo maximo
        fluxoMaximo += fluxoCaminho
        v = fim
 
        # atualizando valores no grafo de folgas
        while v != origem:
            u = anteriores[v]
            passarFluxo (G, v, u, fluxoCaminho)
            passarFluxo (G, u, v, -fluxoCaminho)
            v = anteriores[v]
            
    return fluxoMaximo