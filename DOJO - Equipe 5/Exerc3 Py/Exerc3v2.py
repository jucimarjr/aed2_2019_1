lista = []


#str = string, l = index primeiro elemento, r = index ulitmo elemento=========
def permutate(str, l, r):

    if l == r:
        lista.append(''.join(str))
    else:
        for i in range(l, r+1):
            str[l], str[i] = str[i], str[l]
            permutate(str, l + 1, r)
            str[l], str[i] = str[i], str[l] #Backtrack

#===============================================================================

arquivo = open('Entrada3.txt', 'r')

#Termos de 1 ate n
n = int(arquivo.readline())
#n = 5

strin = ""
for i in range(0, n):
    strin = strin + str(i+1)


strin = list(strin)
print(strin)
permutate(strin, 0, len(strin)-1)

#==========================================FILTRO PARA DESARRANJO==========================================
zero = []
for i in range(n):
    zero.append(0)
zero = tuple(zero)

for i in range(0, n):
    for j in range(0, len(lista)):
        if lista[j][i] == lista[0][i] and j != 0:
            lista[j] = zero

for i in range(0, lista.count(zero)):
    lista.remove(zero)
lista.remove(lista[0])

#=========================================================================================================

printar = open('Saida3.txt', 'w')

temp = []
listaf = []

for i in range(len(lista)): #Dividir em lista
    for j in range(n):
        temp.append(int(lista[i][j]))
    listaf.append(list(temp))
    temp.clear()

for i in range(len(lista)): #Escrever em txt a listaa
    printar.write(str(lista[i])+"\n")


arquivo.close()
printar.close()
