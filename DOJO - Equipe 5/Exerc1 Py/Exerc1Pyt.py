arquivo = open('Entrada1.txt', 'r')

#Termos de 1 ate n
n = int(arquivo.readline())

#K em k numeros de combinacoes
k = int(arquivo.readline())

#print(n)
#print(k)

termos = []
lista = []

#for i in range(n):
#    termos.append(n+1)

termos = range(1,n+1)

#def valid()


def comb(termos, combin):

    lista = tuple(termos) #cria uma lista de tupla com os termos
    n = len(lista)

    if combin > n: #nao fara nada, existira mais termos que combinacoes
        return

    indice = list(range(combin))
    yield tuple(lista[i] for i in indice) #vai retornar uma tupla que tera os numeros da lista, de 0 ate combin

    while True:
        for i in reversed(range(combin)):
            if indice[i] != i + n - combin:
                break
        else:
            return
        indice[i] += 1
        for j in range(i+1, combin):
            indice[j] = indice[j-1] + 1
        yield tuple(lista[i] for i in indice)




printar = open('Saida1.txt', 'w')
comb = comb(termos,k)
for i in list(comb):
    printar.write(str(i)+"\n")


arquivo.close()
printar.close()