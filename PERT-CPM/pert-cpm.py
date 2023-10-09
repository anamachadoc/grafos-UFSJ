import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import numpy as np

# reading an directed graph
G = nx.read_weighted_edgelist("graph.txt", nodetype = int, create_using=nx.DiGraph())
vert = list(G.nodes)
edges = list(G.edges)
vertices = []
# Earliest Start Time (EST) and Latest Start Time (LST)
for vertice in vert:
    vertices.append ({"vertice": vertice, "EST": 0, "LST": 1000})
weightEdges = []
for edge in edges:
    weightEdges.append((nx.get_edge_attributes (G, "weight")[edge]))

'''
plotting the input graph
nx.draw_spectral(
    G, 
    with_labels = True,
    node_size = 300,
    node_color = 'pink',
    )
plt.show()

'''

for vertice in vert:
    for i in range(len(edges)): 
        if (edges[i][1] == vertice): # vertice eh alcancado por outro
            newEST = vertices[edges[i][0]-1].get("EST") + weightEdges[i]
            if (newEST > vertices[vertice-1].get("EST")):
                vertices[vertice-1]["EST"] = newEST
fila =  []     
for vertice in vert: # encontrando o ultimo vertice do grafo
    cont = 0
    for i in range(len(edges)): 
        if vertice != edges[i][0]:
            cont = cont + 1
    if cont == len(edges):
        fila.append(vertice)
        vertices[vertice-1]["LST"] = vertices[vertice-1]["EST"]

for vertice in fila:
    for i in range(len(edges)):
        if (edges[i][1] == vertice): # quem alcanca ele
            antecessor = edges[i][0]
            weightEdges = (nx.get_edge_attributes (G, "weight")[edges[i]])
            newLST = vertices[vertice-1]["LST"] - weightEdges
            if (vertices[antecessor-1]["LST"] > newLST):
                vertices[antecessor-1]["LST"] = newLST
            if antecessor not in fila:
                fila.append(antecessor)
for vertice in vertices:
    print (vertice)
     
        