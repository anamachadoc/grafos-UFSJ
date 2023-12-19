import networkx as nx
import funcoesAuxiliares as f
import matplotlib.pyplot as plt

G = f.lendoEntrada()
grafoResposta = G.copy()

# definindo o layout para as plotagens
pos = nx.kamada_kawai_layout(G)
# plotando grafo de entrada
nx.draw(
        G,
        pos =  pos,
        with_labels = True,
        font_size = 5,
        node_size = 60,
        node_color = '#8EE5EE',    
        )
plt.savefig("entrada.jpg")

verticesCamera = [] 
naoMonitoradas = list(G.edges())
ruasMonitoradas = {}  
    
# definir esquinas com cameras
while (naoMonitoradas != []):
    conjuntoVertices = f.ordenarVertices(G)
    vertice = conjuntoVertices.pop(0) 
    posCamera = vertice[1] # vertice que deve conter uma camera
    verticesCamera.append(posCamera)
    f.monitorarRuas (G, posCamera, ruasMonitoradas, naoMonitoradas)
    G.remove_node(posCamera)

# verificando se ha esquinas com cameras desnecessarias
f.verificarCamerasInuteis(grafoResposta, verticesCamera, ruasMonitoradas)

# grafo de saida
color = f.criandoGrafoSaida(grafoResposta, verticesCamera)
f.criandoSaida(grafoResposta, verticesCamera, ruasMonitoradas) 
pos = nx.kamada_kawai_layout(grafoResposta)

# plotando o grafo de saida
nx.draw(
        grafoResposta,
        pos =  pos,
        with_labels = True,
        font_size = 5,
        node_size = 60,
        node_color = color,    
        )
plt.savefig("resultado.png")
    