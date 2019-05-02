def Combinacao(lista, numero):
    n = numero
    combinacoes = []
    combinacao = []

    for i in range(len(lista) - (n-1)):
        sentinela = lista[i]
        for j in range((i),(len(lista)-(n-1))):
            combinacao.append(sentinela)
            cont = 1
            while (cont < numero):
                combinacao.append(lista[j+cont])
                cont+=1
            combinacoes.append(combinacao)
            combinacao=[]

    return combinacoes

print(Combinacao([1,2,3,4,5,6,7,8,9], 2))