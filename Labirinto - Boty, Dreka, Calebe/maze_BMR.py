import random as rand
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore


class Maze(QWidget):

    def __init__(self):
        super(Maze, self).__init__()

        altura_labirinto = QLabel('Altura: ')
        largura_labirinto = QLabel('Largura: ')
        nomes = QLabel('Nomes: ')
        botaoCria = QPushButton("Labirinto", self)

 
        
        

        self.altura_labirinto_Edit = QLineEdit("0")
        self.largura_labirinto_Edit = QLineEdit("0")
        self.entradax_labirinto_Edit = QLineEdit("0")
        self.entraday_labirinto_Edit = QLineEdit("0")
        self.saidax_labirinto_Edit = QLineEdit(str(int(self.altura_labirinto_Edit.text())-1))
        self.saiday_labirinto_Edit = QLineEdit(str(int(self.largura_labirinto_Edit.text())-1))
        self.nomes_Edit = QLineEdit("")
        botaoCria.clicked.connect(self.buttonClicked)


#Deixando o PyQT bonitinho
        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(altura_labirinto, 0, 0)
        grid.addWidget(self.altura_labirinto_Edit, 0, 1)

        grid.addWidget(largura_labirinto, 2, 0)
        grid.addWidget(self.largura_labirinto_Edit, 2, 1)

        grid.addWidget(nomes, 3, 0)
        grid.addWidget(self.nomes_Edit, 3, 1)

      

        grid.addWidget(botaoCria, 4, 1)
        self.setLayout(grid)
#       ================================================

        self.setGeometry(300, 300, 350, 300) #Tamanho
        self.setWindowTitle('MAZE_BMR') #Titulo
        self.setWindowIcon(QtGui.QIcon ('smile.png'))
        self.setFont(QtGui.QFont('SansSerif', 20)) # change font type and size
        
        #print (self.style () .objectName())
       # self.styleChoice = QtGui.QLabel("Windowns Vista",self)
        self.show() #Mostrar

        

    def buttonClicked(self):  


        
        altura = int(self.altura_labirinto_Edit.text())
        largura = int(self.largura_labirinto_Edit.text())

       
        entradax = 0
        entraday = 0

        saidax = altura
        saiday = largura

        
        plt.figure('Labirinto original')
        plt.axes().invert_yaxis()
        plt.figure('Resposta de saída do Labirinto original')
        plt.axes().invert_yaxis()
        

#Garante que todos os nós estarão denttro da matriz
        if entradax < 0:
            entradax = 0
        if entraday < 0:
            entraday = 0
        if saidax < 0:
            saidax = 0
        if saiday < 0:
            saiday = 0

        if entradax > altura - 1:
            entradax = altura - 1
        if entraday > largura - 1:
            entraday = largura - 1
        if saidax > altura - 1:
            saidax = altura - 1
        if saiday > largura - 1:
            saiday = largura - 1



        vert = []
        num_vert = 0

        for i in range(altura):
            vert.append([])
            for j in range(largura):
                vert[i].append(num_vert)
                num_vert += 1

        adjacencia = []
        rand.seed()

        # Inicia adjacências
        for i in range(altura*largura):
            adjacencia.append([])
            for j in range(altura*largura):
                adjacencia[i].append(0)

        # Faz a matriz adjacência e cada posição será um nó, desse nó verifica-se as arestas direcionadas
        for i in range(altura):
            for j in range(largura):
                if j+1 < largura:  # direita, se existir
                    adjacencia[vert[i][j]][vert[i][j+1]] = int(rand.random() * 99)+1  
                if j-1 >= 0:  # esquerda, se existir                        
                    adjacencia[vert[i][j]][vert[i][j-1]] = int(rand.random() * 99)+1  
                if i+1 < altura:  # de cima, se existir
                    adjacencia[vert[i][j]][vert[i+1][j]] = int(rand.random() * 99)+1
                if i-1 >= 0:  # de baixo, se existir
                    adjacencia[vert[i][j]][vert[i-1][j]] = int(rand.random() * 99)+1


        cont = 0
        for i in range(altura*largura):
            for j in range(cont):
                adjacencia[i][j] = adjacencia[j][i]
            cont += 1

        #Prim


        def procurar_vertice(vertices, desejado):
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
                                entrada_aresta = largura_aresta  # Entrada eh a largura da adjacencia(entrada)

            return menor, saida_aresta, entrada_aresta

        # Matriz de vertices visitados para o algoritmo de PRIM, inicia-se ele com o vertice que se começa
        visitado = [0]

        # Adjancecia do labirinto de árvore mínima
        adjacencia_menor = []
        # Inicia adjacências
        for i in range(altura*largura):
            adjacencia_menor.append([])
            for j in range(altura*largura):
                adjacencia_menor[i].append(0)

        #somente se visitar tudo que para
        while len(visitado) != altura*largura:
            peso, saida_vertice, entrada_vertice = procurar_menor_aresta(visitado, adjacencia)
            visitado.append(entrada_vertice)
            adjacencia_menor[saida_vertice][entrada_vertice] = peso
            adjacencia_menor[entrada_vertice][saida_vertice] = peso


        #Djikstra

        vert_dji = []
        
        for i in range(altura):
            vert_dji.append([])
            for j in range(largura):
                vert_dji[i].append(9999)


        vert_dji[entradax][entraday] = 0

        nao_visitado_dji = []
        for i in range(altura*largura):
            nao_visitado_dji.append(i)

        visitado_dji = []
        proximo = [nao_visitado_dji.pop(vert[entradax][entraday])]  
        proximo_bloco = []


        # ou para depois de tudo visitado ou quando chegar na posição final
        while len(visitado_dji) != altura*largura and len(proximo) != 0:
            if proximo[0] == vert[saidax][saiday]:
                visitado_dji.append(proximo.pop(0))
                break

            for i in range(altura*largura):
                if adjacencia_menor[proximo[0]][i] > 0:  # Passa pela matriz de adjecencias e verifica qual caminho tomar
                    x, y = procurar_vertice(vert, i)  # Funcao que retorna o vertice da aresta
                    if vert_dji[x][y] > adjacencia_menor[proximo[0]][i] and vert_dji[x][y] == 9999:
                        x_atual, y_atual = procurar_vertice(vert, proximo[0])  # Se o caminho não foi tomado, será o proximo
                        vert_dji[x][y] = vert_dji[x_atual][y_atual] + 1  # O proximo vertice será o anterior + 1
                        proximo_bloco.append(i)  # Adiciona-se à pilha de próximos
                        nao_visitado_dji.remove(i)  # Retira-se dos não visitados

            # Retira do proximo e coloca no visitado
            visitado_dji.append(proximo.pop(0))
            if len(proximo) == 0:  # Se o bloco de proximos acabar, adiciona-se outro
                proximo = proximo_bloco
                proximo_bloco = []


#Quando conseguir chegar até a saída, então ele faz o caminho de volta marcando até a entrada

        adjacencia_dji = [[saidax, saiday]]
        atual_x = saidax
        atual_y = saiday

        # Enquanto não chegar ao começo, não para
        while (atual_x != entradax) or (atual_y != entraday):
            for i in range(largura*altura):  # Visitar todos os possíveis adjacentes
                if adjacencia_menor[vert[atual_x][atual_y]][i] > 0:  # Ver quais disponiveis
                    proximo_x, proximo_y = procurar_vertice(vert, i)  # Guardar a disponivel
                    if vert_dji[proximo_x][proximo_y] < vert_dji[atual_x][atual_y]:
                        #Ver se a disponível é menor(é o caminho certo)
                        adjacencia_dji.insert(0, [atual_x, atual_y])  # Se sim, adicionar às adjacencias
                        atual_x, atual_y = proximo_x, proximo_y  # Passar ao proximo

        adjacencia_dji.insert(0, [entradax, entraday])

       
        resposta = []  

        # montando os labirintos aqui
        for i in range((altura*2)+1):
            resposta.append([])
            for j in range((largura*2)+1):
                resposta[i].append(0)
             

        #alterar dimensão para melhor visualização

        for i in range(altura):
            for j in range(largura):
                resposta[(i * 2) + 1][(j * 2) + 1] = 1
              


        #paredes
        for i in range(altura*largura):
            for j in range(altura*largura):
                if adjacencia_menor[i][j] != 0:
                    x_i, y_i = procurar_vertice(vert, i)
                    x_i, y_i = (x_i * 2) + 1, (y_i * 2) + 1
                    x_j, y_j = procurar_vertice(vert, j)
                    x_j, y_j = (x_j * 2) + 1, (y_j * 2) + 1
                    resposta[int((x_i + x_j) / 2)][int((y_i + y_j) / 2)] = 1
                    

        for i in range(len(visitado_dji)):
            resp_x, resp_y = procurar_vertice(vert, visitado_dji[i])
            resp_x, resp_y = (resp_x * 2) + 1, (resp_y * 2) + 1
           
            

        vetor_resposta = []

        
        for i in range(len(adjacencia_dji) - 1):
            resp_x, resp_y = adjacencia_dji[i]
            resp_x, resp_y = (resp_x * 2) + 1, (resp_y * 2) + 1
            vetor_resposta.append([resp_x, resp_y])

            anterior_x, anterior_y = adjacencia_dji[i]
            posterior_x, posterior_y = adjacencia_dji[i + 1]
            anterior_x, anterior_y = (anterior_x * 2) + 1, (anterior_y * 2) + 1
            posterior_x, posterior_y = (posterior_x * 2) + 1, (posterior_y * 2) + 1
            if resposta[int((anterior_x + posterior_x) / 2)][int((anterior_y + posterior_y) / 2)] == 1:
                vetor_resposta.append([int((anterior_x + posterior_x) / 2), int((anterior_y + posterior_y) / 2)])

        for i in range(len(vetor_resposta)):
            resp_x, resp_y = vetor_resposta[i]
            resposta[resp_x][resp_y] = 2

          
        resposta[(entradax * 2) + 1][(entraday * 2) + 1] = 3
        resposta[(saidax * 2) + 1][(saiday * 2) + 1] = 4


        
        labirinto = []
        for i in range((altura*2)+1):
            labirinto.append([])
            for j in range((largura*2)+1):
                labirinto[i].append(0)


        for i in range(altura):
            for j in range(largura):
                labirinto[(i*2)+1][(j*2)+1] = 1

   
        for i in range(altura*largura):
            for j in range(altura*largura):
                if adjacencia_menor[i][j] != 0:
                    x_i, y_i = procurar_vertice(vert, i)
                    x_i, y_i = (x_i * 2) + 1, (y_i * 2) + 1
                    x_j, y_j = procurar_vertice(vert, j)
                    x_j, y_j = (x_j * 2) + 1, (y_j * 2) + 1
                    labirinto[int((x_i+x_j)/2)][int((y_i+y_j)/2)] = 1

        labirinto[(entradax * 2) + 1][(entraday * 2) + 1] = 2
        labirinto[(saidax * 2) + 1][(saiday * 2) + 1] = 3



    
        cores = (["#551A8B", "#F0FFFF", "#7FFFD4", "#7FFF00"])
        cmap = ListedColormap(cores)
        plt.figure('Labirinto original')
        plt.pcolormesh(labirinto, cmap=cmap)
        plt.axis("equal")
        plt.xticks([])
        plt.yticks([])
      
        
     
        cores = (["#551A8B", "#F0FFFF", "#FFB90F", "#7FFFD4", "#7FFF00"])
        cmap = ListedColormap(cores)
        plt.figure('Resposta de saída do Labirinto original')
        plt.pcolormesh(resposta, cmap=cmap)
        plt.axis("equal")
        plt.xticks([])
        plt.yticks([])
      

        plt.show()


#main
app = QApplication([])
ex = Maze()
app.exec_()
