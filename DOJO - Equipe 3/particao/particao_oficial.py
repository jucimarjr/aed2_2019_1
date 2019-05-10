def particoes(lista):
    if not lista:
        yield []
    else:
        a, *T = lista
        for particao in particoes(T):
            yield particao + [[a]]
            for i, conjunto in enumerate(particao):
                yield particao[:i] + [conjunto + [a]] + particao[i+1:]

for particao in particoes([1,2,3]):
    print(particao)




