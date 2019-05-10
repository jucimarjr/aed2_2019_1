lista = []

def permutate(vetor, l, r):

    if l == r:
        lista.append(''.join(vetor))
    else:
        for i in range(l, r+1):
            vetor[l],vetor[i] = vetor[i], vetor[l]
            permutate(vetor, l + 1, r) 
            vetor[l], vetor[i] = vetor[i], vetor[l]
num = 4
strin = "1"
for i in range(1,num):
    strin = strin + str(i+1)

strin = list(strin)
permutate(strin, 0, len(strin)-1)

print(lista)
