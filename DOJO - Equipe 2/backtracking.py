import sys

class tour_cavaleiros:
    def __init__(self, width, height):
        """
        Funcao de start, contendo altura e largura ou seja linhas e colunas da matriz,
        declaracao do nome da matriz e chamada da funcao de criacao do tabuleiro
        """
        self.w = width
        self.h = height

        self.tabuleiro = []
        self.gerar_tabuleiro()

    def gerar_tabuleiro(self):
        """
        Cria uma linha aninhada para representar o tabuleiro
        """
        for i in range(self.h):
            self.tabuleiro.append([0]*self.w)

    def print_tabuleiro(self):
        """
        Funcao de print do tabuleiro
        """       
        print ("  ")
        print ("------")
        for elem in self.tabuleiro:
            print (elem)
        print ("------")
        print ("  ")

    def gerar_movimentos_possiveis(self, cur_pos):
        """
        Gerador de lista de movimentos aceitos que um cavalo pode fazer a seguir
        """
        posicao_possivel = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]
        """
        Nessas conficoes verificam se o movimento sai do tabuleiro
        """
        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if (new_x >= self.h):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue
            else:
                posicao_possivel.append((new_x, new_y))

        """
        Retorna o vetor de possiveis posicoes
        """
        return posicao_possivel

    def sortir_vizinhos_sozinhos(self, to_visit):
        """
        Eh mais eficiente visitar primeiro os vizinhos de canto,
        uma vez que estes estao nas bordas do tabuleiro de xadrez e nao pode
        ser alcancado facilmente se feito mais tarde na travessia
        """
        lista_vizinhos = self.gerar_movimentos_possiveis(to_visit)
        empty_neighbours = []

        for vizinhos in lista_vizinhos:
            np_value = self.tabuleiro[vizinhos[0]][vizinhos[1]]
            if np_value == 0:
                empty_neighbours.append(vizinhos)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.gerar_movimentos_possiveis(empty)
            for m in moves:
                if self.tabuleiro[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)


        """
        Organiza o vetor de visitas
        """
        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours

    def tour(self, n, caminho, to_visit):
        """
        Recursao do tour dos cavalos. Inputs sao os seguintes:
        n = eh a atual arvore de busca em profundidade
        caminho = caminho atual
        to_visit = no a ser visitado
        """
        self.tabuleiro[to_visit[0]][to_visit[1]] = n
        caminho.append(to_visit) #acrescente o vertice mais recente ao ponto atual 
        print ("Visitando: ", to_visit)

        if n == self.w * self.h: #se todo o tabuleiro foi percorrido
            self.print_tabuleiro()
            print (caminho)
            print ("Pronto!")
            sys.exit(1)

        else:
            """
            Backtracking ocorre quando a funcao fica voltando aqui com valores diferentes pro n
            """
            sorted_neighbours = self.sortir_vizinhos_sozinhos(to_visit)
            for vizinhos in sorted_neighbours:
                self.tour(n+1, caminho, vizinhos)

            #Se sair desse loop, todos os vizinhos deram errado, entao o resetamos
            self.tabuleiro[to_visit[0]][to_visit[1]] = 0
            try:
                caminho.pop()
                print ("Voltando para: ", caminho[-1])
            except IndexError:
                print ("Caminho nao encontrado")
                sys.exit(1)

if __name__ == '__main__':
    #Input definindo o tamanho do tabuleiro e chamada das funcoes
    n = int(input("Tamanho do tabuleiro: "))
    kt = tour_cavaleiros(n, n)
    kt.tour(1, [], (0,0))
kt.print_tabuleiro()
