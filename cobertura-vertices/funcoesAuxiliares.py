import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def lendoEntrada():
    G = nx.read_gml('sjdr.gml', label = None)
    return G


def ordenarVertices(G): # funcao que ordena os vertices de acordo com quantas ruas cada um pode monitorar
    conjuntoVertices = [] # lista de listas contendo em cada lista o numero de arestas que podem ser monitoradas por um vertice e esse vertice
    for node in G.nodes():
        conjuntoVertices.append([G.degree(node), node])
    conjuntoVertices.sort (reverse = True)
    return conjuntoVertices

def monitorarRuas (G, posCamera, ruasMonitoradas, naoMonitoradas): # funcao que remove as ruas monitoradas por posCamera do conjunto de ruas nao monitoadas
    ruas = list(G.edges(posCamera))
    ruasMonitoradas[posCamera] = ruas
    for rua in ruas:
        ida = rua
        volta = (rua[1], rua[0])
        try:
            naoMonitoradas.remove(ida)
        except:
            naoMonitoradas.remove(volta)
            
def verificarCamerasInuteis(G, verticesCamera, ruasMonitoradas):
    for ponto in verticesCamera:
        flag = 0
        arestasAdjacentes = list(G.edges(ponto))
        for rua in arestasAdjacentes:
            if (rua[1] not in verticesCamera):
                flag = 1
                break
        if flag == 0: # removendo ponto com camera desnecessaria, pois todos seus adjacentes possuem cameras
            ruasMonitoradas.pop(ponto)
            for rua in arestasAdjacentes:
                ruasMonitoradas[rua[1]].append(rua) # redistribuindo as ruas marcadas como monitoradas por esse ponto
            verticesCamera.remove(ponto)
        
def criandoSaida(G, verticesCamera, ruasMonitoradas):
    with open('monitoramento.txt', 'w') as output:
        output.write(f'Numero de cameras necessarias: {len(verticesCamera)}')
        output.write('\n')
        for esquina in ruasMonitoradas:
            output.write(f'Rua(s) arestas pela camera em {esquina}:')
            output.write('\n')
            ruas = ruasMonitoradas[esquina]
            for i in range(len(ruas)):
                nome = G[ruas[i][0]][ruas[i][1]].get('name', None)
                output.write(f'- {ruas[i]}: {nome}')
                output.write('\n')
                
def criandoGrafoSaida(Final, verticesCamera):
    color = []
    semCamera = []
    for node in Final.nodes():
        if node in verticesCamera:
            color.append('pink')
        else:
            color.append('#8EE5EE')
    legend_elements = [Line2D([0], [0], marker='o', color='#8EE5EE', label='Sem Camera', lw=0,
                            markerfacecolor='#8EE5EE', markersize=10),
                    Line2D([0], [0], marker='o', color='pink', label='Com Camera', lw=0,
                            markerfacecolor='pink', markersize=10)]
    ax = plt.gca()
    ax.legend(handles=legend_elements, loc='upper right')
    return color