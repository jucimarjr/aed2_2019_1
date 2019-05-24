'''
1 Start with a random string of 28 characters.
2 Make 100 copies of the string (reproduce).
3 For each character in each of the 100 copies, with a probability of 5%, replace (mutate) the character with a new random character.
4 Compare each new string with the target string "METHINKS IT IS LIKE A WEASEL", and give each a score (the number of
  letters in the string that are correct and in the correct position).
5 If any of the new strings has a perfect score (28), halt. Otherwise, take the highest scoring string, and go to step 2.
'''

import random as rd
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class ScrollMessageBox(QMessageBox): #Funcao do scroll message box
   def __init__(self, l, *args, **kwargs):
      QMessageBox.__init__(self, *args, **kwargs)
      scroll = QScrollArea(self)
      scroll.setWidgetResizable(True)
      self.content = QWidget()
      scroll.setWidget(self.content)
      lay = QVBoxLayout(self.content)
      for item in l:
         lay.addWidget(QLabel(item, self)) #Adiciona os itens a caixa
      self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
      self.setStyleSheet("QScrollArea{min-width:500 px; min-height: 600px}")
      self.setWindowTitle('Resultado')


class Weasel(QWidget):

    def __init__(self):
        super().__init__()

#       ============CRIACAO DOS LABELS, CAIXA DE TEXTO E BOTOES========
        taxa = QLabel('Taxa de mutação: ')
        numero_copia = QLabel('Copia por geração: ')
        frase = QLabel('Frase desejada: ')
        go_button = QPushButton("Go!", self)

        self.taxaEdit = QLineEdit("5")
        self.numeroEdit = QLineEdit("1000")
        self.fraseEdit = QLineEdit("ME THINKS IT IS LIKE A WEASEL")
        go_button.clicked.connect(self.buttonClicked)


#       ==============FORMATACAO======================
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(taxa, 1, 0)
        grid.addWidget(self.taxaEdit, 1, 1)

        grid.addWidget(numero_copia, 2, 0)
        grid.addWidget(self.numeroEdit, 2, 1)

        grid.addWidget(frase, 3, 0)
        grid.addWidget(self.fraseEdit, 3, 1)

        grid.addWidget(go_button)
        self.setLayout(grid)
#       ================================================

        self.setGeometry(300, 300, 350, 300) #Tamanho
        self.setWindowTitle('Weasel') #Titulo
        self.show() #Mostrar


    def buttonClicked(self): #QUANDO O BOTAO FOR CLICADO

#       =================================FUNCOES=============================
        # copia[0] = copia da frase
        # copia[1] = nota da frase
        def iniciar_copia(copias, n_copias):
            for i in range(n_copias):
                copias[0].append("")  # Inicia o vetor da copia
                copias[1].append(0)  # Nota da iteracao, por enquanto se deixa 0

        # Copiar a string nas copias, pois se aplicara a mutacao em seguida
        def gerar_nova_copia(copias, string_copiada):
            for i in range(len(copias[0])):
                copias[0][i] = string_copiada

        #Substitui o caracter de uma frase
        def recolocar(frase, caracter, pos):
            temp = list(frase)
            temp[pos] = caracter

            return "".join(temp)

        # Atribuir uma nota a uma string
        def atribuir_nota_string(string, original):
            nota = 0
            for i in range(len(string)):
                if string[i] == original[i]:
                    nota += 1
            return nota

        # Encontrar o index da maior nota da lista
        def encontrar_index_maior_nota(copias):
            max = 0
            for i in range(len(copias[1])):
                if copias[1][i] > max:
                    max = i

            return max

        # Aplicar uma mutacao a todas as copias
        def aplicar_mutacao_e_nota(copias, string_desejado):
            for i in range(len(copias[0])):
                for j in range(len(copias[0][0])):
                    chance_mutacao = rd.random() * 100  # numero entre 0 e 100
                    if chance_mutacao < taxa_mutacao:  # Mutacao ocorre

                        # Se mutacao acontecer, ele pega um caracter aleatorio e substitui
                        copias[0][i] = recolocar(copias[0][i], candidatos[int(rd.random() * len(candidatos))], j)

                copias[1][i] = atribuir_nota_string(copias[0][i], string_desejado) #Dar uma nota

#       =====================================================================

        # Por centagem de mutacao
        taxa_mutacao = float(self.taxaEdit.text()) #Pega o texto da caixa de texto

        # String desejada
        string_desejado = self.fraseEdit.text() #Pega o texto da caixa de texto

        # Numero de copias por geracao
        n_copia = int(self.numeroEdit.text()) #Pega o texto da caixa de texto

        # Candidatos para se usar na string inicial aleatoria
        candidatos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

        rd.seed()

        string_inicial = ""

        # Gera um numero entre 0 e o tamanho da string desejada
        # Usando como base os candidatos, ele pega o numero gerado para criar uma string inicial aleatoria
        for i1 in range(len(string_desejado)):
            string_inicial += candidatos[int(rd.random() * len(candidatos))]

        copia = [[], []]

        # Inicia a matriz de copia
        iniciar_copia(copia, n_copia)

        # A string da geracao sera a string com maior nota
        string_geracao = string_inicial

        lista_geracao = [[], [], []]  # Criar a lista da geracao para o resultado

        lista_geracao[0].append(string_inicial)  # String da geracao 0
        lista_geracao[1].append(0)  # Numero da Geracao 0
        lista_geracao[2].append(atribuir_nota_string(string_inicial, string_desejado))  # Nota da string dessa geracao


        #Loop que so acabara quando a nota da copia for perfeita
        while(True):
            gerar_nova_copia(copia, string_geracao) #Gero uma nova copia com a string selecionada

            aplicar_mutacao_e_nota(copia, string_desejado) #Aplica-se uma mutacao a ela e da uma nota ao mutado

            string_geracao = copia[0][encontrar_index_maior_nota(copia)] #Uma nova string da geracao sera selecionado

            lista_geracao[0].append(string_geracao) #Adicionar a string da geracao na lista
            lista_geracao[1].append(max(lista_geracao[1]) + 1) #Dar um nome a geracao, no caso, ultima geracao + 1
            lista_geracao[2].append(atribuir_nota_string(string_geracao, string_desejado))

            if atribuir_nota_string(string_geracao, string_desejado) == len(string_desejado): #Se a nota do string atual == string desejado
                break

        listaprint = []
        # Print das geracoes
        for i in range(len(lista_geracao[0])):
            listaprint.append("Geracao [" + str(lista_geracao[1][i]) + "]: " + str(lista_geracao[0][i]) + ", Nota: [" + str(lista_geracao[2][i]) + "]")

#        Printar o resultado em um scrollbox
        result = ScrollMessageBox(listaprint, None)

#        Janela so fecha quando usuario clicar
        result.exec_()

#=======================MAIN==========================

#Iniciar uma aplicacao
app = QApplication([])
#Iniciar o programa "weasel"
ex = Weasel()
#Fechar apenas com o clique do usuario
app.exec_()
