def Fatorial(num):
    fat = 1
    if num == 0:
        return 1
    while num > 1:
        fat = fat * num
        num-=1
    return fat

def Permutacao(lista):
    combinacoes = []
    combinacao = lista
    topper = 0
    i = 0
    swapi = 0
    while (i < (Fatorial(len(lista)))):
        if (swapi == len(lista) - 1):
            swapi = 0
        aux = combinacao[swapi]
        combinacao[swapi] = combinacao[swapi + 1]
        combinacao[swapi + 1] = aux
        combinacoes.append(combinacao)
        print(combinacao, "\n")
        swapi+=1
        i+=1
    return sorted(combinacoes)

Permutacao([1,2,3,4]),
