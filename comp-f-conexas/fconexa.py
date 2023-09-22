import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# reading an directed graph
G = nx.read_edgelist("graph.txt", create_using=nx.DiGraph())
vertices = list(G.nodes)
edges = list(G.edges)

# plotting the graph
nx.draw_circular(
    G, 
    with_labels = True,
    node_size = 300,
    node_color = 'pink',
    )
plt.show()

# function to find the direct transitive closure
def verifica_plus (v): 
    fecho_dir = [v] 
    for vertice in fecho_dir: # for all vertices in closure
        for i in range(len(edges)): # for all vertices in the graph
            if edges[i][0] == vertice and edges[i][1] not in fecho_dir:
                fecho_dir.append(edges[i][1])
    return fecho_dir

# function to find the inverse transitive closure
def verifica_minus (v): 
    fecho_inv = [v] 
    for vertice in fecho_inv:  
        for i in range(len(edges)): 
            if edges[i][1] == vertice and edges[i][0] not in fecho_inv:
                fecho_inv.append(edges[i][0])
    return fecho_inv

# algorithm strongly connected component
result = [] 
r_plus = [] # R+
r_minus = [] # R-
while len(vertices) != 0:
    component = [] # list of current component vertices
    v = vertices[0]
    r_plus = verifica_plus(v) # direct transitive closure
    r_minus = verifica_minus(v) # inverse transitive closure
    auxiliar = []
    for vt in vertices:
        if vt in r_minus and vt in r_plus: # intersection of r_minus and r_plus means this vertice is in the component
            component.append(vt) 
        else:
            auxiliar.append(vt)
    result.append (component)
    vertices = auxiliar # only vertices that aren't in the component remain in the vertice list
    
# output
output = open("comp-f-conexas.txt", 'w')
print ("\n ha", len(result), "componentes f-conexas! sao elas:\n")  
output.write (str(len(result))+" componentes f-conexas:\n")
for compf in result:
    print(compf, "\n")
    output.write ("[ ")
    for vert in compf:
        output.write("'" + vert + "' ")
    output.write ("]")
    output.write("\n")
output.close() 

  