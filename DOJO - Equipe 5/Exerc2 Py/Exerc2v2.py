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

arquivo = open('Entrada2.txt', 'r')

#Termos de 1 ate n
n = int(arquivo.readline())
#n = 5


strin = ""
for i in range(0, n):
    strin = strin + str(i+1)


strin = list(strin)
print(strin)
permutate(strin, 0, len(strin)-1)

printar = open('Saida2.txt', 'w')

#printar.write(str(lista)+"\n")
#print(lista)

temp = []
listaf = []

for i in range(len(lista)): #Dividir em lista
    for j in range(n):
        temp.append(int(lista[i][j]))
    listaf.append(list(temp))
    temp.clear()

for i in range(len(lista)): #Printar em txt
    printar.write(str(lista[i])+"\n")


arquivo.close()
printar.close()
