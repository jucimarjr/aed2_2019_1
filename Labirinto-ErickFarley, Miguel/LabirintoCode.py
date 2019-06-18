from tkinter import *
import random as rand
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def clickButton(alturaIn, larguraIn):  

    # ================================INICIALIZAÇÕES================================================

    # Numero de casas, altura x largura = numero de vertices
    altura = int(alturaIn)
    largura = int(larguraIn)

    vert = []
    num_vert = 0

    # Cria a matriz de vertices e da um alturaLabel a eles
    for i in range(altura):
        vert.append([])
        for j in range(largura):
            vert[i].append(num_vert)
            num_vert += 1


    adjacencia = []
    rand.seed()

    # Inicia adjacências com 0
    for i in range(altura*largura):
        adjacencia.append([])
        for j in range(altura*largura):
            adjacencia[i].append(0)

    # Criar matriz de adjacencia, utilizando valores randomicos
    for i in range(altura):
        for j in range(largura):
            if j+1 < largura: 
                adjacencia[vert[i][j]][vert[i][j+1]] = int(rand.random() * 99)+1 
            if j-1 >= 0:          
                adjacencia[vert[i][j]][vert[i][j-1]] = int(rand.random() * 99)+1 
            if i+1 < altura:
                adjacencia[vert[i][j]][vert[i+1][j]] = int(rand.random() * 99)+1
            if i-1 >= 0: 
                adjacencia[vert[i][j]][vert[i-1][j]] = int(rand.random() * 99)+1

    # Cria uma matriz espelhada na diagonal principal, transformar direciondo em não direcionado
    cont = 0
    for i in range(altura*largura):
        for j in range(cont):
            adjacencia[i][j] = adjacencia[j][i]
        cont += 1

    # ======================================PRIM===========================================  
    def retorna_posi_vertice(vertices, desejado):
        for altura_vert in range(len(vertices)):
            for largura_vert in range(len(vertices[0])):
                if vertices[altura_vert][largura_vert] == desejado:
                    return altura_vert, largura_vert


    def procurar_menor_aresta(visitado, adjacencia):
        saida_aresta = 0
        entrada_aresta = 0
        for altura_aresta in range(len(visitado)):  # visitar todos os vertices da lista visitado
            menor = 100
            for largura_aresta in range(altura*largura):  # visitar todas as possibilidades daquela aresta
                if adjacencia[visitado[altura_aresta]][largura_aresta] > 0:  # Apenas pegar aresta não 0
                    if menor > adjacencia[visitado[altura_aresta]][largura_aresta]:  # Pegar o menor das arestas
                        if largura_aresta not in list(visitado):  # So passa se o vertice que queremos ir nao estiver nos visitados
                            menor = adjacencia[visitado[altura_aresta]][largura_aresta]
                            saida_aresta = visitado[altura_aresta]  # Saida sera o vertice em que se está analisando
                            entrada_aresta = largura_aresta 

        return menor, saida_aresta, entrada_aresta

    # Matriz de vertices visitados para o algoritmo de PRIM, inicia-se ele com o vertice que se começa
    visitado = [0]

    # Adjancecia do labirinto de árvore mínima
    adjacenciaArvMin = []
    # Inicia adjacências
    for i in range(altura*largura):
        adjacenciaArvMin.append([])
        for j in range(altura*largura):
            adjacenciaArvMin[i].append(0)

    #Só para quando tiver visitado tudo
    while len(visitado) != altura*largura:
        peso, saida_vertice, entrada_vertice = procurar_menor_aresta(visitado, adjacencia)
        visitado.append(entrada_vertice)
        adjacenciaArvMin[saida_vertice][entrada_vertice] = peso
        adjacenciaArvMin[entrada_vertice][saida_vertice] = peso


    # =======================DJISKTRA============================

    verticesDjikstra = []
    # Cria adjacências
    for i in range(altura):
        verticesDjikstra.append([])
        for j in range(largura):
            verticesDjikstra[i].append(9999)

    # [0][0] é o ponto inicial
    verticesDjikstra[0][0] = 0

    djikstraNaoVisitados = []
    for i in range(altura*largura):
        djikstraNaoVisitados.append(i)

    visitadosDjikstra = []
    proximo = [djikstraNaoVisitados.pop(0)]
    proximosVertices = []


    # Vai parar ao visitar todos os vertices ou chegar na posiçao final
    while len(visitadosDjikstra) != altura*largura and len(proximo) != 0:
        if proximo[0] == (altura*largura) - 1:
            visitadosDjikstra.append(proximo.pop(0))
            break

        for i in range(altura*largura):
            if adjacenciaArvMin[proximo[0]][i] > 0:  # Passa pela matriz de adjecencias e verifica qual caminho tomar
                x, y = retorna_posi_vertice(vert, i)  # Funcao que retorna o vertice da aresta
                if verticesDjikstra[x][y] > adjacenciaArvMin[proximo[0]][i] and verticesDjikstra[x][y] == 9999:
                    X_Atual, Y_Atual = retorna_posi_vertice(vert, proximo[0])  # Se o caminho não foi tomado, será o proximo
                    verticesDjikstra[x][y] = verticesDjikstra[X_Atual][Y_Atual] + 1  # O proximo vertice será o anterior + 1
                    proximosVertices.append(i)  # Adiciona-se à pilha de próximos
                    djikstraNaoVisitados.remove(i)  # Retira-se dos não visitados

        # O vertice e removido do proximo e é adicionado em visitados
        visitadosDjikstra.append(proximo.pop(0))
        if len(proximo) == 0:  # Se o bloco de proximos acabar, adiciona-se outro
            proximo = proximosVertices
            proximosVertices = []


    # =============================Saida Labirinto=============================
    # Após percorrer com Djikstra, é necessário fazer o caminho contrário para definir o caminho correto

    adjacencia_djisktra = [[altura - 1, largura - 1]]
    Xatual = altura - 1
    Yatual = largura - 1
    Xproximo = 0
    Yproximo = 0

    while (Xatual != 0) or (Yatual != 0):
        menorResposta = int(verticesDjikstra[Xatual][Yatual])
        if Yatual+1 < largura: 
            if verticesDjikstra[Xatual][Yatual + 1] == menorResposta - 1:
                Xproximo, Yproximo = Xatual, Yatual + 1

        if Yatual-1 >= 0: 
            if verticesDjikstra[Xatual][Yatual - 1] == menorResposta - 1:
                Xproximo, Yproximo = Xatual, Yatual - 1

        if Xatual+1 < altura: 
            if verticesDjikstra[Xatual + 1][Yatual] == menorResposta - 1:
                Xproximo, Yproximo = Xatual + 1, Yatual

        if Xatual-1 >= 0: 
            if verticesDjikstra[Xatual - 1][Yatual] == menorResposta - 1:
                Xproximo, Yproximo = Xatual - 1, Yatual

        Xatual = Xproximo
        Yatual = Yproximo
        menorResposta -= 1
        adjacencia_djisktra.insert(0, [Xatual, Yatual])


    tentativa = [] 
    respostaLab = [] 

    #======================================Configuracao e Plot do Labirinto================================

    # Iniciar os labirintos
    for i in range((altura*2)+1):
        respostaLab.append([])
        tentativa.append([])
        for j in range((largura*2)+1):
            respostaLab[i].append(0)
            tentativa[i].append(0)

    # "Aumentar" labirinto para que fique com tamanho correto para o plot
    for i in range(altura):
        for j in range(largura):
            respostaLab[(i * 2) + 1][(j * 2) + 1] = 1
            tentativa[(i * 2) + 1][(j * 2) + 1] = 1

    # Entradas e saidas do labirinto
    respostaLab[1][0] = 2
    respostaLab[len(respostaLab)-2][len(respostaLab[0])-1] = 2
    tentativa[1][0] = 2
    tentativa[len(tentativa)-2][len(tentativa[0])-1] = 2

    # Levantamento das paredes
    for i in range(altura*largura):
        for j in range(altura*largura):
            if adjacenciaArvMin[i][j] != 0:
                x_i, y_i = retorna_posi_vertice(vert, i)
                x_i, y_i = (x_i * 2) + 1, (y_i * 2) + 1
                x_j, y_j = retorna_posi_vertice(vert, j)
                x_j, y_j = (x_j * 2) + 1, (y_j * 2) + 1
                respostaLab[int((x_i + x_j) / 2)][int((y_i + y_j) / 2)] = 1
                tentativa[int((x_i + x_j) / 2)][int((y_i + y_j) / 2)] = 1

    # Plot de todas as casas visitadas
    for i in range(len(visitadosDjikstra)):
        resp_x, resp_y = retorna_posi_vertice(vert, visitadosDjikstra[i])
        resp_x, resp_y = (resp_x * 2) + 1, (resp_y * 2) + 1
        tentativa[resp_x][resp_y] = 2

    # Plot de todas as casas do caminho correto
    for i in range(len(adjacencia_djisktra)):
        resp_x, resp_y = adjacencia_djisktra[i]
        resp_x, resp_y = (resp_x * 2) + 1, (resp_y * 2) + 1
        respostaLab[resp_x][resp_y] = 2

    # Preenchimento entre as casas do caminho correto
    for i in range(len(adjacencia_djisktra)-1):
        anterior_x, anterior_y = adjacencia_djisktra[i]
        posterior_x, posterior_y = adjacencia_djisktra[i+1]
        anterior_x, anterior_y = (anterior_x * 2) + 1, (anterior_y * 2) + 1
        posterior_x, posterior_y = (posterior_x * 2) + 1, (posterior_y * 2) + 1
        if respostaLab[int((anterior_x + posterior_x) / 2)][int((anterior_y + posterior_y) / 2)] == 1:
            respostaLab[int((anterior_x + posterior_x) / 2)][int((anterior_y + posterior_y) / 2)] = 2

    #print labirinto
    labirinto = []
    for i in range((altura*2)+1):
        labirinto.append([])
        for j in range((largura*2)+1):
            labirinto[i].append(0)

    for i in range(altura):
        for j in range(largura):
            labirinto[(i*2)+1][(j*2)+1] = 1

    #Entrada do labirinto
    labirinto[1][0] = 2
    #Saida do labirinto
    labirinto[len(labirinto)-2][len(labirinto[0])-1] = 1


    for i in range(altura*largura):
        for j in range(altura*largura):
            if adjacenciaArvMin[i][j] != 0:
                x_i, y_i = retorna_posi_vertice(vert, i)
                x_i, y_i = (x_i * 2) + 1, (y_i * 2) + 1
                x_j, y_j = retorna_posi_vertice(vert, j)
                x_j, y_j = (x_j * 2) + 1, (y_j * 2) + 1
                labirinto[int((x_i+x_j)/2)][int((y_i+y_j)/2)] = 1

    #Usa Matplot para imprimir o labirinto

    cores = (["black", "white", "red"])
    cmap = ListedColormap(cores)
    plt.figure(0)
    plt.pcolormesh(labirinto, cmap=cmap)
    plt.axis("off")
    plt.xticks([])
    plt.yticks([])

    plt.figure(1)
    plt.pcolormesh(respostaLab, cmap=cmap)
    plt.axis("off")
    plt.xticks([])
    plt.yticks([])


    plt.show()
