def Imprime_comb(vetor, n, k): #n tamanho do vetor
    vet = [0]*k
    comb(vetor, vet, 0, n-1, 0, k)


def comb(vetor, vet, comeco, final, index, k):
    if (index == k):
        for j in range(k):
            print(vet[j], final = " ")
        print()
        return

    i = comeco
    while(i <= final and final - i + 1 >= k - index):
        vet[index] = vetor[i]
        comb(vetor, vet, i+1, final, index + 1, k)
        i += 1    


print("Qual o tamanho do vetot?: ")
tam = int(input())
vet=[]

for i in range(tam):
    print ("Insira o elemento", i ,"no vetor: ")
    x = int(input())
    vet.append(x)

print("Digite o k")
k = int(input())

Imprime_comb(vet,tam,k)