def permutacao(lista):
    #se a lista estiver vazia, então não tem permutação
    if len(lista)==0:
        return []
    #se a lista conter apenas 1 valor, ele retorna esse unico elemento
    if len(lista)==1:
        return [lista]

    l = []

    #repete o input e calcula a permutaçnao
    for i in range(len(lista)):
        m = lista[i]
        #remove m ou lista[i] da lista.
        final = lista[:i] + lista[i+1:]
        #gera as permutações onde m é o primeiro elemento
        for p in permutacao(final):
            l.append([m] + p)
    return l

#aqui insere o valor, ex: 123
entrada = input("insira o valor: ")
#transforma a entrada em lista
result = list(entrada)

for p in permutacao(result):
    print(p)
