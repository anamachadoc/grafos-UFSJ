import networkx as nx
import matplotlib.pyplot as plt
import igraph as ig

# create an directed graph
G = nx.DiGraph()

# vertices
vertices = [0, 1, 2, 3, 4, 5, 6, 7]
G.add_nodes_from (vertices)

# edges
edges = [ (1, 2), (1, 3), (3, 4), (5, 6), (7,5), (6,7)]
G.add_edges_from (edges)

# output
S = nx.DiGraph()

# function to r_plus
def fr_plus (edges, v):
    aux = []
    for edge in edges:
        if edge[0] == v:
            aux.append(edge[1])
    return aux

# function  to r_minus
def fr_minus (edges, v):
    aux = []
    for edge in edges:
        if edge[1] == v:
            aux.append(edge[0])
    return aux

def verifica (r_plus, v):
    fecho_dir = []
    ver = fr_plus (edges, v)
    for i in ver:
        if i not in edges:
            fecho_dir.append(i)
    return (fecho_dir)

# algorithm
k = 0
vert = [] # list of current component vertices
list = [] # auxiliar list of vertices
r_plus = [] # R+
r_minus = [] # R-
while len(vertices != 0):
    v = vertices[k]
    vert.append (list)
    r_plus.append (v)
    r_minus.append (v)
    while len(verifica(r_plus, v)) != 0:
        vert[0] = verifica(r_plus, v)
        r_plus += vert[0]
    
    

