import random as rand
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from PyQt5.QtWidgets import *


class Labirinto(QWidget):

    def __init__(self):
        super().__init__()

#       ============CRIACAO DOS LABELS, CAIXA DE TEXTO E BOTOES========
        altura_labirinto = QLabel('Altura do Labirinto: ')
        largura_labirinto = QLabel('Largura do Labirinto: ')
        entrada_labirinto = QLabel('ENTRADA: ')
        entradax_labirinto = QLabel('X: ')
        entraday_labirinto = QLabel('Y: ')
        saida_labirinto = QLabel('SAIDA: ')
        saidax_labirinto = QLabel('X: ')
        saiday_labirinto = QLabel('Y: ')
        criar_button = QPushButton("Criar", self)

        self.check = QCheckBox("Mostrar alcance Djisktra", self)
        self.check.toggle()

        self.altura_labirinto_Edit = QLineEdit("5")
        self.largura_labirinto_Edit = QLineEdit("5")
        self.entradax_labirinto_Edit = QLineEdit("0")
        self.entraday_labirinto_Edit = QLineEdit("0")
        self.saidax_labirinto_Edit = QLineEdit(str(int(self.altura_labirinto_Edit.text())-1))
        self.saiday_labirinto_Edit = QLineEdit(str(int(self.largura_labirinto_Edit.text())-1))
        criar_button.clicked.connect(self.buttonClicked)


#       ==============FORMATACAO======================
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(altura_labirinto, 1, 0)
        grid.addWidget(self.altura_labirinto_Edit, 1, 1)

        grid.addWidget(largura_labirinto, 2, 0)
        grid.addWidget(self.largura_labirinto_Edit, 2, 1)

        grid.addWidget(entrada_labirinto, 3, 0)
        grid.addWidget(entradax_labirinto, 3, 1)
        grid.addWidget(self.entradax_labirinto_Edit, 3, 2)
        grid.addWidget(entraday_labirinto, 3, 3)
        grid.addWidget(self.entraday_labirinto_Edit, 3, 4)

        grid.addWidget(saida_labirinto, 4, 0)
        grid.addWidget(saidax_labirinto, 4, 1)
        grid.addWidget(self.saidax_labirinto_Edit, 4, 2)
        grid.addWidget(saiday_labirinto, 4, 3)
        grid.addWidget(self.saiday_labirinto_Edit, 4, 4)

        grid.addWidget(self.check, 5, 0)

        grid.addWidget(criar_button, 6, 0)
        self.setLayout(grid)
#       ================================================

        self.setGeometry(300, 300, 350, 300) #Tamanho
        self.setWindowTitle('Labirinto') #Titulo
        self.show() #Mostrar

        #plt.figure(0)
        #plt.axes().invert_yaxis()
        #plt.figure(1)
        #plt.axes().invert_yaxis()
        #plt.figure(2)
        #plt.axes().invert_yaxis()

    def buttonClicked(self):  # QUANDO O BOTAO FOR CLICADO

        # ================================INICIALIZAÇÕES================================================

        # Numero de casas, altura x largura = numero de vertices
        altura = int(self.altura_labirinto_Edit.text())
        largura = int(self.largura_labirinto_Edit.text())

        entradax = int(self.entraday_labirinto_Edit.text())
        entraday = int(self.entradax_labirinto_Edit.text())

        saidax = int(self.saiday_labirinto_Edit.text())
        saiday = int(self.saidax_labirinto_Edit.text())

        plt.figure(0)
        plt.axes().invert_yaxis()
        plt.figure(1)
        plt.axes().invert_yaxis()
        plt.figure(2)
        plt.axes().invert_yaxis()

        # =============Impedir que os valores estejam fora da matriz de vertices======
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

        # ==============================================================================

        vert = []
        num_vert = 0

        # Cria a matriz de vertices e da um nome a eles
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

        # Criar matriz de adjacencia, ele sera direcionado
        # Ele pega a matriz de verticies e coloca na matriz de adjecencias suas possibilidades de movimento
        # ex: 0 pode ir para 1(sua direita) e 3(abaixo) se for um 3x3
        for i in range(altura):
            for j in range(largura):
                if j+1 < largura:  # vertice a direita, se existir
                    adjacencia[vert[i][j]][vert[i][j+1]] = int(rand.random() * 99)+1  #Peso das arestas, podem ir de 1 a 100
                if j-1 >= 0:  # vertice a esquerda, se existir                        #Esta aleatoriedade cria labirintos
                    adjacencia[vert[i][j]][vert[i][j-1]] = int(rand.random() * 99)+1  # aleatorios
                if i+1 < altura:  # vertice acima, se existir
                    adjacencia[vert[i][j]][vert[i+1][j]] = int(rand.random() * 99)+1
                if i-1 >= 0:  # vertice abaixo, se existir
                    adjacencia[vert[i][j]][vert[i-1][j]] = int(rand.random() * 99)+1

        # Cria uma matriz espelhada na diagonal principal, transformr direciondo em não direcionado
        cont = 0
        for i in range(altura*largura):
            for j in range(cont):
                adjacencia[i][j] = adjacencia[j][i]
            cont += 1

        # ===============================ALGORITMO DE PRIM===========================================


        #Está função pega a matriz de verticies e retorna as cordenadas do valor que queremos
        #     [0][1][2] nesta matriz 3x3, se escolhermos 3, ele retorna [1][0]
        # Ex: [3][4][5]
        #     [6][7][8]
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

        #Só para quando tiver visitado tudo
        while len(visitado) != altura*largura:
            peso, saida_vertice, entrada_vertice = procurar_menor_aresta(visitado, adjacencia)
            visitado.append(entrada_vertice)
            adjacencia_menor[saida_vertice][entrada_vertice] = peso
            adjacencia_menor[entrada_vertice][saida_vertice] = peso


        # =======================DJISKTRA============================

        vert_djisktra = []
        # Inicia adjacências
        for i in range(altura):
            vert_djisktra.append([])
            for j in range(largura):
                vert_djisktra[i].append(9999)

        # [0][0] é o ponto de partida
        vert_djisktra[entradax][entraday] = 0

        nao_visitado_dji = []
        for i in range(altura*largura):
            nao_visitado_dji.append(i)

        visitado_dji = []
        proximo = [nao_visitado_dji.pop(vert[entradax][entraday])]  # retirar numero em que está a posicao de entrada
        proximo_bloco = []


        # Vai parar se já foi visistado TUDO, ou break quando chegar na posição final
        while len(visitado_dji) != altura*largura and len(proximo) != 0:
            # Parar se o djisktra chegar na posicao final
            if proximo[0] == vert[saidax][saiday]:
                visitado_dji.append(proximo.pop(0))
                break

            for i in range(altura*largura):
                if adjacencia_menor[proximo[0]][i] > 0:  # Passa pela matriz de adjecencias e verifica qual caminho tomar
                    x, y = procurar_vertice(vert, i)  # Funcao que retorna o vertice da aresta
                    if vert_djisktra[x][y] > adjacencia_menor[proximo[0]][i] and vert_djisktra[x][y] == 9999:
                        x_atual, y_atual = procurar_vertice(vert, proximo[0])  # Se o caminho não foi tomado, será o proximo
                        vert_djisktra[x][y] = vert_djisktra[x_atual][y_atual] + 1  # O proximo vertice será o anterior + 1
                        proximo_bloco.append(i)  # Adiciona-se à pilha de próximos
                        nao_visitado_dji.remove(i)  # Retira-se dos não visitados

            # Retira-se do proximo e coloca no visitado
            visitado_dji.append(proximo.pop(0))
            if len(proximo) == 0:  # Se o bloco de proximos acabar, adiciona-se outro
                proximo = proximo_bloco
                proximo_bloco = []


        # ============RETORNO DO CAMINHO DE DJISKTRA(PRA RESPOSTA)=============
        # Depois que se consegue o caminho correto através do djisktra, o único jeito de fazer o caminho correto
        # é fazer o pecurso contrário.
        #
        # Descomente esse print para ver porque deve ser feito no caminho inverso
        #for i in range(len(vert_djisktra)):
        #    print(vert_djisktra[i])

        adjacencia_djisktra = [[saidax, saiday]]
        atual_x = saidax
        atual_y = saiday

        # Enquanto não chegar ao começo, não para
        while (atual_x != entradax) or (atual_y != entraday):
            for i in range(largura*altura):  # Visitar todas as possibilidades de adjacencias do local
                if adjacencia_menor[vert[atual_x][atual_y]][i] > 0:  # Ver quais disponiveis
                    proximo_x, proximo_y = procurar_vertice(vert, i)  # Guardar a disponivel
                    if vert_djisktra[proximo_x][proximo_y] < vert_djisktra[atual_x][atual_y]:
                        #Ver se a disponível é menor(é o caminho certo)
                        adjacencia_djisktra.insert(0, [atual_x, atual_y])  # Se sim, adicionar às adjacencias
                        atual_x, atual_y = proximo_x, proximo_y  # Passar ao proximo

        adjacencia_djisktra.insert(0, [entradax, entraday])

        labirinto_tentativa = []  # Labirinto das tentativas
        labirinto_resposta = []  # Labirinto do caminho correto

        # Iniciar os labirintos
        for i in range((altura*2)+1):
            labirinto_resposta.append([])
            labirinto_tentativa.append([])
            for j in range((largura*2)+1):
                labirinto_resposta[i].append(0)
                labirinto_tentativa[i].append(0)

        # "Aumentar" labirinto para que fique com tamanho correto para o plot
        for i in range(altura):
            for j in range(largura):
                labirinto_resposta[(i * 2) + 1][(j * 2) + 1] = 1
                labirinto_tentativa[(i * 2) + 1][(j * 2) + 1] = 1


        # Levantamento das paredes
        for i in range(altura*largura):
            for j in range(altura*largura):
                if adjacencia_menor[i][j] != 0:
                    x_i, y_i = procurar_vertice(vert, i)
                    x_i, y_i = (x_i * 2) + 1, (y_i * 2) + 1
                    x_j, y_j = procurar_vertice(vert, j)
                    x_j, y_j = (x_j * 2) + 1, (y_j * 2) + 1
                    labirinto_resposta[int((x_i + x_j) / 2)][int((y_i + y_j) / 2)] = 1
                    labirinto_tentativa[int((x_i + x_j) / 2)][int((y_i + y_j) / 2)] = 1

        # Plot de todas as casas visitadas
        for i in range(len(visitado_dji)):
            resp_x, resp_y = procurar_vertice(vert, visitado_dji[i])
            resp_x, resp_y = (resp_x * 2) + 1, (resp_y * 2) + 1
            labirinto_tentativa[resp_x][resp_y] = 2
            #if self.check.isChecked():
                #labirinto_resposta[resp_x][resp_y] = 3

        vetor_resposta = []

        # Plot de todas as casas do caminho correto
        for i in range(len(adjacencia_djisktra) - 1):
            resp_x, resp_y = adjacencia_djisktra[i]
            resp_x, resp_y = (resp_x * 2) + 1, (resp_y * 2) + 1
            vetor_resposta.append([resp_x, resp_y])

            anterior_x, anterior_y = adjacencia_djisktra[i]
            posterior_x, posterior_y = adjacencia_djisktra[i + 1]
            anterior_x, anterior_y = (anterior_x * 2) + 1, (anterior_y * 2) + 1
            posterior_x, posterior_y = (posterior_x * 2) + 1, (posterior_y * 2) + 1
            if labirinto_resposta[int((anterior_x + posterior_x) / 2)][int((anterior_y + posterior_y) / 2)] == 1:
                #labirinto_resposta[int((anterior_x + posterior_x) / 2)][int((anterior_y + posterior_y) / 2)] = 2
                vetor_resposta.append([int((anterior_x + posterior_x) / 2), int((anterior_y + posterior_y) / 2)])

        # Caminho da resposta
        for i in range(len(vetor_resposta)):
            resp_x, resp_y = vetor_resposta[i]
            labirinto_resposta[resp_x][resp_y] = 2

        # Entradas e saidas do labirinto_tentativa
        labirinto_tentativa[(entradax * 2) + 1][(entraday * 2) + 1] = 3
        labirinto_tentativa[(saidax * 2) + 1][(saiday * 2) + 1] = 4

        # Entradas e saidas do labirinto_resposta
        #if self.check.isChecked():
            #labirinto_resposta[(entradax * 2) + 1][(entraday * 2) + 1] = 4
            #labirinto_resposta[(saidax * 2) + 1][(saiday * 2) + 1] = 5
        #else:
        labirinto_resposta[(entradax * 2) + 1][(entraday * 2) + 1] = 3
        labirinto_resposta[(saidax * 2) + 1][(saiday * 2) + 1] = 4


        # ==================================PLOT LABIRINTO============================================
        # print labirinto
        labirinto = []
        for i in range((altura*2)+1):
            labirinto.append([])
            for j in range((largura*2)+1):
                labirinto[i].append(0)


        #for i in range((altura*2)+1):
        #    print(labirinto[i])

        for i in range(altura):
            for j in range(largura):
                labirinto[(i*2)+1][(j*2)+1] = 1

        # Entrada do labirinto
        #labirinto[1][0] = 1
        # Saida do labirinto
        #labirinto[len(labirinto)-2][len(labirinto[0])-1] = 1


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


        cores = (["black", "white", "orange", "red"])
        cmap = ListedColormap(cores)
        plt.figure(0)
        plt.pcolormesh(labirinto, cmap=cmap)
        plt.axis("equal")
        plt.xticks([])
        plt.yticks([])
        #plt.axes().invert_yaxis()

        if self.check.isChecked():
            cores = (["black", "white", "yellow", "orange", "red"])
            cmap = ListedColormap(cores)
            plt.figure(1)
            plt.pcolormesh(labirinto_tentativa, cmap=cmap)
            plt.axis("equal")
            plt.xticks([])
            plt.yticks([])
            #plt.axes().invert_yaxis()

        cores = (["black", "white", "blue", "orange", "red"])
        cmap = ListedColormap(cores)
        plt.figure(2)
        plt.pcolormesh(labirinto_resposta, cmap=cmap)
        plt.axis("equal")
        plt.xticks([])
        plt.yticks([])
        #plt.axes().invert_yaxis()

        plt.show()


# =======================MAIN==========================

# Iniciar uma aplicacao
app = QApplication([])
# Iniciar o programa "weasel"
ex = Labirinto()
# Fechar apenas com o clique do usuario
app.exec_()
