# coding: utf-8
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from math import inf
from queue import PriorityQueue
#ALUNOS : ANTONIO RODRIGUES DE SOUZA NETO , THIAGO SANTOS BORGES , NADINE BRITO
#classe onde definimos a célula do labirinto, sua estrutura e propriedades
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #Cima, Baixo, Direita, Esquerda  
        self.muros = [1,1,1,1] # Todas as paredes estão no início
        self.borda = [0,0,0,0]
        self.visitado = False

    def desenhar_cell(self):
        if self.muros[0] == 1:
            plt.hlines(y=self.y, xmin=self.x, xmax=self.x+1, linewidth=1, color='white')
        if self.muros[1] == 1:
            plt.vlines(x=self.x+1, ymin=self.y, ymax=self.y+1, linewidth=1, color='white')
        if self.muros[2] == 1:
            plt.hlines(y=self.y+1, xmin=self.x, xmax=self.x+1, linewidth=1, color='white')
        if self.muros[3] == 1:
            plt.vlines(x=self.x, ymin=self.y, ymax=self.y+1, linewidth=1, color='white')

    def ajustar_borda(self,xmax,ymax):
        if self.y == 0: 
            self.borda[0] = 1
        if self.x == xmax: 
            self.borda[1] = 1
        if self.y == ymax: 
            self.borda[2] = 1
        if self.x == 0: 
            self.borda[3] = 1


# GERAÇÃO DO LABIRINTO
def gerar_lab(altura, largura):
    celulas = [[0 for y in range(0, altura)] for x in range(0, largura)]

    # Inicializa todos os muros
    for y in range(0, altura):
        for x in range(0, largura):
            c = Cell(x, y)
            c.ajustar_borda(largura - 1, altura - 1)
            celulas[x][y] = c

    # inicia a célula
    pilha = []
    num_total = largura * altura
    num_visitado = 0  
    celula_atual = celulas[np.random.randint(0, largura)][np.random.randint(0, altura)]
    num_visitado += 1

    while num_visitado < num_total:
        vizinhos_com_paredes = verificar_vizinhos(celulas, celula_atual, celula_atual.x, celula_atual.y)
        num = len(vizinhos_com_paredes)
        if num > 0:
            rand_vizinho = vizinhos_com_paredes[np.random.randint(0, num)]
            eliminar_muro(celula_atual, rand_vizinho)
            pilha.append(celula_atual)
            celula_atual = rand_vizinho
            num_visitado += 1
        else:
            cell = pilha.pop()
            celula_atual = cell

    for y in range(0, altura):
        for x in range(0, largura):
            c = celulas[x][y]
            c.desenhar_cell()

    return celulas

#função que compara a posição que célula está, para ir para uma direção diferente dos muros
def eliminar_muro(celula, vizinho):
    if vizinho.y == celula.y-1:
        celula.muros[0] = 0
        vizinho.muros[2] = 0
        return
    if vizinho.x == celula.x+1:
        celula.muros[1] = 0
        vizinho.muros[3] = 0
        return
    if vizinho.y == celula.y+1:
        celula.muros[2] = 0
        vizinho.muros[0] = 0
        return
    if vizinho.x == celula.x-1:
        celula.muros[3] = 0
        vizinho.muros[1] = 0
        return

# Obtém a rota da solução do labirinto para qualquer ponto
def rota(celulas, iniciox, inicioy, fimx, fimy):
    celula_inicio = celulas[iniciox][inicioy]
    celula_fim = celulas[fimx][fimy]
    pilha = []
    celula_atual = celula_inicio
    celula_atual.visitado = True
    while celula_atual != celula_fim:
        vizinhos = vizinhos_nao_visitados(celulas, celula_atual)
        num = len(vizinhos)
        if num > 0:
            rand_vizinho = vizinhos[randint(0, num) - 1]
            rand_vizinho.visitado = True
            pilha.append(celula_atual)
            celula_atual = rand_vizinho
        else:
            celula = pilha.pop()
            celula_atual = celula

    for c in pilha:
        plt.plot(c.x + 0.5, c.y + 0.5, linestyle='None', marker="s", color="r")
    plt.plot(celula_inicio.x + 0.5, celula_inicio.y + 0.5, linestyle='None', marker="o", color="g", markersize=15)
    plt.plot(celula_fim.x + 0.5, celula_fim.y + 0.5, linestyle='None', marker="o", color="g", markersize=15)
def dijkstra(graph, root):

    queue = PriorityQueue()  # Lista de prioridades

    path = {}  # DicionÃ¡rio com o caminho e o custo total
    for v in graph.vertices():
        if v == root:
            path[v] = [[], 0]  # Custo 0 para o root
        else:
            path[v] = [[], inf]  # Custo infinito para os demais

        queue.put((path[v][1], v))  # Adiciona todas na lista de prioridade (maior prioridade = menor custo)

    remaing_vertices = list(graph.vertices())  # lista de vertices nao visitados

    for i in range(len(graph.vertices())):
        u = queue.get()[1]  # vertice prioritario da lista
        remaing_vertices.remove(u)  # remove da lista de nao visitados

        for v in remaing_vertices:  # para cada v nao visitado
            du = path[u][1]  # menor custo ate vertice u (prioritario)
            w = graph.direct_cost(u, v)  # custo de u ate v
            dv = path[v][1]  # menor custo ate vertice v
            if du + w < dv:  # O caminho ate v pelo u menos custoso que o melhor ate entao
                path[v][1] = du + w  # Atualiza o custo
                path[v][0] = path[u][0] + [u]  # Atualiza o caminho
                queue.queue.remove((dv, v))  # Atualiza a prioridade do vertice v na lista de prioridade
                queue.put((path[v][1], v))

    return path
def prim(graph, root):
    vertex = [root]  # Lista dos vertices a partir do qual buscamos as arestas
    selected_edges = []  # Lista com as arestas selecionadas
    weight = 0  # Peso do minimum spanning tree

    remaing_vertices = list(graph.vertices())  # Lista com os vertices destinos da busca
    remaing_vertices.remove(root)  # O root eh ponto de partida, entao sai da lista

    for i in range(len(remaing_vertices)):  # Devemos buscar |V| - 1 vertices
        min_cost = inf  # Inicializamos o custo minimo como infinito
        va, vb = None, None  # Vertices candidatos para a aresta selecionada
         #Vertices que nao sao selecionados
        for v1 in vertex:  # Para cada vertice na lista de busca origem
            for v2 in remaing_vertices:  # Buscamos os vertices que ainda nao estao no grafo final
                cost = graph.direct_cost(v1, v2)  # Calcula o custo da aresta
                if cost < min_cost:  # Se for menor que o minimo ate entao, atualizamos os dados
                    va = v1
                    vb = v2
                    min_cost = cost

        if min_cost < inf:  # Depois de todas as buscas, se o custo eh finito:
            selected_edges.append((va, vb, min_cost))  # Adicionamos a aresta de va a vb na solucao
            vertex.append(vb)  # vb agora sera nova origem de busca
            remaing_vertices.remove(vb)  # vb nao mais sera destino de busca, pois ja consta na solucao
            weight += min_cost  # Atualiza o peso

    return selected_edges, weight  # Retorna a lista de arestas selecionadas com o peso total

#função para verificar espaços disponiveis, devido as paredes do labirinto
def verificar_vizinhos(cells, cell_atual, x, y):
    vizinhos = []
    if cell_atual.borda[0] == 0:
        nt = cells[x][y-1]
        if nt.muros == [1,1,1,1]:
            vizinhos.append(nt)
    if cell_atual.borda[1] == 0:
        nr = cells[x+1][y]
        if nr.muros == [1,1,1,1]:
            vizinhos.append(nr)
    if cell_atual.borda[2] == 0:
        nb = cells[x][y+1]
        if nb.muros == [1,1,1,1]:
            vizinhos.append(nb)
    if cell_atual.borda[3] == 0:
        nl = cells[x-1][y]
        if nl.muros == [1,1,1,1]:
            vizinhos.append(nl)
    return vizinhos

def vizinhos_nao_visitados(celulas, c):
    list_vizinhos = []
    if c.borda[0] == 0 and c.muros[0] == 0:
        vizinho = celulas[c.x][c.y-1]
        if not vizinho.visitado:
            list_vizinhos.append(vizinho)
    if c.borda[1] == 0 and c.muros[1] == 0:
        vizinho = celulas[c.x+1][c.y]
        if not vizinho.visitado:
            list_vizinhos.append(vizinho)
    if c.borda[2] == 0 and c.muros[2] == 0:
        vizinho = celulas[c.x][c.y+1]
        if not vizinho.visitado:
            list_vizinhos.append(vizinho)
    if c.borda[3] == 0 and c.muros[3] == 0:
        vizinho = celulas[c.x-1][c.y]
        if not vizinho.visitado:
            list_vizinhos.append(vizinho)
    return list_vizinhos


#tamanho do labirinto
largura = 20
altura = 20


plt.figure(0) 
celulas = gerar_lab(altura, largura)
plt.axis([0, largura, altura, 0])
ax = plt.gca()
ax.set_facecolor('xkcd:black')
ax.set_facecolor((0,0,0))
#plt.gca().invert_yaxis()
rota(celulas, 0, 0, largura-1, altura-1)
plt.show()




