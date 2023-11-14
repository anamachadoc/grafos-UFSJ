for node in G.nodes():
    A['vertice'].append(node)
    A['numAdjacentes'].append(G.out_degree(node))
    
print (A['vertice'])
print ('\n\n\n')
print (A['numAdjacentes'])


 cont = 0
for edge in G.edges():
    print(edge[0])