import numpy as np


def proximo_movimento(position, n):

    offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    moves = [tuple(np.add(position, offset)) for offset in offsets]
    moves = [move for move in moves
             if all(coord in range(0, n) for coord in move)]

    return moves


def proximo_movimento_possivel(position, n, board):
    return [move for move in proximo_movimento(position, n) if board[move] == 0]


def proximos_movimentos_ordernado(position, n, board):
    moves = sorted([(len(proximo_movimento_possivel(move, n, board)), move)
                    for move in proximo_movimento_possivel(position, n, board)])
    return [move[1] for move in moves]


def definir_cavalo_campo(board, position, k):

    board[position] = k

    # Resolvido
    if 0 not in board:
        return board

    #testar movimentos do cavalo
    for move in proximos_movimentos_ordernado(position, n, board):

        ret = definir_cavalo_campo(board, move, k+1)
        if ret is not None:
            board = ret
            return board

    #Back track
    board[position] = 0

    return None

#Main
arquivo = open('Entrada1.txt', 'r')
printar = open('Saida5.txt', 'w')

n = int(arquivo.readline())
#n = 5
board = np.zeros((n, n))
board = definir_cavalo_campo(board, (0, 0), 1)
#print(board)
printar.write(str(board))

arquivo.close()
printar.close()

