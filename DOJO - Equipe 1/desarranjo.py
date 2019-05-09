#Algoritmo de Desarranjo ou permutação caotica

def desarranjo(posicao, entrada , visitados, resposta): #recebe uma posição, o vetor de entrada, o vetor de visitados e o vetor de respostas
    if (posicao == len(entrada)): #se a posicação for igual ao tamanho do vetor de entrada significa que ele terminou e imprime a resposta
        print (resposta)
    for i in range(len(entrada)): 
        if ((i != posicao) and (visitados[i]==0)): #o vetor de visitados marca quais ele ja passou
            visitados[i] = 1
            resposta[posicao] = entrada[i]
            desarranjo(posicao+1, entrada, visitados, resposta) #chamada recursiva para a proxima posicação do vetor
            visitados[i] = 0 #zera a posição 
    
entrada = [1, 2, 3, 4] #recebe um valor de entrada
visitados = [0]*len(entrada) #cria-se um vetor de visitados do tamanho do vetor de entrada
resposta = [-1]*len(entrada) #cria um vetor resposta, do tamanho da ultima posicação do vetor de entrada, ou seja, n-1
desarranjo(0, entrada, visitados, resposta) #passa-se como parametros para a função: 0, como posição inicial, um vetor de entrada, um de visitados e um de resposta