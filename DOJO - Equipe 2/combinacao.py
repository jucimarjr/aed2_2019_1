def Combinacao(lista, numero):
    #tamanho da combinação
    n = numero
    #Resultado da função, um vetor com vários vetores, onde cada um é uma combinação
    result = []
    #Vetor para armazenar as combinações
    combinacao = []

    #Percorre a lista de entrada  
    for i in range(len(lista) - (n-1)):
        #marca a posição da lista para combinar o restante dos números com ela
        sentinela = lista[i]
        #Percorre o resto da lista.
        for j in range((i),(len(lista)-(n-1))):
            #insere o sentinela em uma combinação
            combinacao.append(sentinela)
            cont = 1
            #Define o tamanho das combinações passado por parâmetro
            while (cont < numero):
                #adiciona as combinações no vetor menor
                combinacao.append(lista[j+cont])
                cont+=1
            #insere o resultado da combinação no vetor final
            result.append(combinacao)
            #Zera o vetor combinação para iniciar uma nova.
            combinacao=[]
    #retorna o vetor com todas as combinações
    return result

print(Combinacao([1,2,3], 2))
