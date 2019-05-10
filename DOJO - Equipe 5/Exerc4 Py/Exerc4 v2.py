#====================================================================================================
def Partition(str, index, out):
    if index == len(str):
        lista.append(out)

    for i in range(index, len(str)):
        Partition(str, i+1, out + "[" + str[index:i+1] + "]")

#====================================================================================================
lista = []

arquivo = open('Entrada4.txt', 'r')

#Termos de 1 ate n
n = int(arquivo.readline())
#n = 5

strin = ""
for i in range(0, n):
    strin = strin + str(i+1)

Partition(strin, 0, "")

printar = open('Saida4.txt', 'w')

for i in range(len(lista)): #Printar em txt
    printar.write(str(lista[i])+"\n")

arquivo.close()
printar.close()
