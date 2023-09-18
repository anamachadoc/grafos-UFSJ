import networkx as nx
import matplotlib.pyplot as plt

# reading an directed graph
G = nx.read_edgelist("graph.txt",create_using=nx.DiGraph())
vertices = list(G.nodes)
edges = list(G.edges)

nx.draw_circular(
    G, 
    with_labels = True,
    node_size = 300,
    node_color = 'pink',
    )
plt.show()
     
def verifica_plus (v):
    fecho_dir = [v] 
    for vertice in fecho_dir:
        for i in range(len(edges)): # rodando para o conjunto de vertices
            if edges[i][0] == vertice and edges[i][1] not in fecho_dir:
                fecho_dir.append(edges[i][1])
    return fecho_dir

def verifica_minus (v):
    fecho_inv = [v] 
    for vertice in fecho_inv:
        for i in range(len(edges)): # rodando para todos os vertices
            if edges[i][1] == vertice and edges[i][0] not in fecho_inv:
                fecho_inv.append(edges[i][0])
    return fecho_inv

# algorithm
result = [] # list of current component vertices
r_plus = [] # R+
r_minus = [] # R-
while len(vertices) != 0:
    list = []
    v = vertices[0]
    r_plus = verifica_plus(v)
    r_minus = verifica_minus(v)
    auxiliar = []
    for vt in vertices:
        if vt in r_minus and vt in r_plus:
            list.append(vt)
        else:
            auxiliar.append(vt)
    result.append (list)
    vertices = auxiliar
print ("\n ha", len(result), "componentes f-conexas! sao elas:", result)   
    
    
    

