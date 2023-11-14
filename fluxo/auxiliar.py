G = {} # G eh o grafo de folgas

# todo vertice possui um dicionario com seus adjacentes e os valores de fluxo das arestas que os ligam
def criarVertice(v): 
    if v not in G.keys():
        G[v] ={}

def adicionarAresta(v, u, fluxo):
    G[v][u] = int(fluxo)
    G[u][v] = int(0)
    
def zerarVisitados (visitado, G):
    v = list(G.keys())
    for vertice in v:
        visitado[vertice] = False
       
def inserirChaves (antecessor, G):
    v = list(G.keys())
    for vertice in v:
        antecessor[vertice] = 'None'
        
def passarFluxo (G, inicio, fim, valorFluxo):
    G[inicio][fim] += valorFluxo
    
# busca em largura para determinar os caminhos
def BFS(G, s, t, antecessor):
    visitado = {}
    zerarVisitados (visitado, G) # a cada novo caminho, todos os vertices devem estar com a chave visitado como False
    fifo = []
    fifo.append(s) # primeiro elemento eh a origem
    visitado[s] = True
 
    while fifo:
        u = fifo.pop(0)
        adj = list(G[u].keys())
        for v in adj: # olha os adjacentes do vertice removido - primeiro da fila
            # adiciona na fila os possiveis = nao visitado e possivel de passar fluxo
            if visitado[v] is False and G[u][v] > 0:
                fifo.append(v)
                visitado[v] = True
                antecessor[v] = u # define o anterior ao elemento adicionado
    # se chegou ate T entao retorna o caminho - se nao quer dizer que todos os caminhos possiveis ja foram olhados
    return True if visitado[t] else False
