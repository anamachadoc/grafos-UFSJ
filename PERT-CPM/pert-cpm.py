import networkx as nx

# reading an directed graph
G = nx.read_weighted_edgelist("graph.txt", nodetype = int, create_using=nx.DiGraph())
vert = list(G.nodes)
edges = list(G.edges)
weightEdges = []
for edge in edges:
    weightEdges.append((nx.get_edge_attributes (G, "weight")[edge]))
    
# dictionary with vertice, Earliest Start Time (EST) and Latest Start Time (LST)
vertices = []
for vertice in vert:
    vertices.append ({"vertice": vertice, "EST": 0.0, "LST": 1000.0})

for vertice in vert:
    for i in range(len(edges)): 
        if (edges[i][1] == vertice): # vertice is edge ending
            newEST = vertices[edges[i][0]-1].get("EST") + weightEdges[i]
            if (newEST > vertices[vertice-1].get("EST")):
                vertices[vertice-1]["EST"] = newEST

# priority queue to find LST's vertices
queue =  []     
vertices[len(vertices)-1]["LST"] = vertices[len(vertices)-1]["EST"]
queue.append(vertices[len(vertices)-1]['vertice']) # the last vertice of the graph is the first in queue
        
for vertice in queue:
    for i in range(len(edges)):
        if (edges[i][1] == vertice): # vertice is edge ending
            antecessor = edges[i][0]
            newLST = vertices[vertice-1]["LST"] - weightEdges[i]
            if (vertices[antecessor-1]["LST"] > newLST):
                vertices[antecessor-1]["LST"] = newLST
            if antecessor not in queue:
                queue.append(antecessor)
    
# define critical path
criticalPath = []
for i in range(len(edges)):
    begin = edges[i][0]
    end = edges[i][1]
    if (vertices[end-1]["LST"] - vertices[begin-1]["EST"] - weightEdges[i] == 0):
        criticalPath.append (edges[i])

# output
for vertice in vertices:
    print (vertice)
print (f"\nFaz parte do caminho critico as arestas:{criticalPath}" )
     
        
