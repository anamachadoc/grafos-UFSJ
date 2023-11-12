import funcoes as f

# reading an directed graph
graph = open('graph.txt')
for line in graph.readlines():
    line = line.split()
    inicio = line[0]
    fim = line[1]
    fluxo = line[2]
    f.criarVertice(inicio)
    f.criarVertice(fim)
    f.adicionarAresta (inicio, fim, fluxo)
# algorithm
fluxoTotal = 0
while (f.G['S']['flag'] == 1):
    caminho = ['S'] # caminho com a unica origem definida
    valorFluxo = []
    f.escolherCaminho ('S', caminho, valorFluxo)
    u = caminho[len(caminho)-1] 
    if (u == 'T'): # consigo chegar ate T
        print(f'fluxo no caminho: {caminho}')
        Fluxo = min(valorFluxo)
        fluxoTotal = fluxoTotal + Fluxo
        print (f'quantidade de fluxo: {Fluxo}')
        f.passarFluxo (caminho, Fluxo)  
print (f.G)
print (f'o fluxo total eh {fluxoTotal}')