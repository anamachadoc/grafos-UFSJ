import funcoes as f
import networkx as nx
import re

G = nx.DiGraph()

# lendo o arquivo de entrada e construindo o grafo
graph = open('sjdr.gml')
line = graph.readlines()
for i in range(len(line)):
    if ('node' in line[i]): # lendo vertice
        ID = line[i+1].split() # ID
        nodeID = int(ID[1])
        labelNode = line[i+2].split() # label
        label = re.sub('"', '', labelNode[1])
        G.add_node(nodeID, label = label)
    elif ('edge' in line[i]): # lendo aresta
        sourceEdge = line[i+1].split()
        source = int(sourceEdge[1])
        targetEdge = line[i+2].split()
        target = int(targetEdge[1])
        nameStreet = re.sub('"', '', line[i+3])
        nameStreet = nameStreet[8:]
        G.add_edge(source, target, name = nameStreet)

A = {
    'vertice': [],
    'numAdjacentes': []
}

for node in G.nodes():
    A['vertice'].append(node)
    A['numAdjacentes'].append(G.out_degree(node))

