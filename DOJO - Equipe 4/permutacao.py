def permutation(list):
    
    if len(list)==0:
        return []
    if len(list)==1:
        return [list]

    l = []

    for i in range(len(list)):
        m = list[i]
        final = list[:i] + list[i+1:]
        for p in permutation(final):
            l.append([m] + p)
    return l

entry = input("insira o valor: ")

result = list(entry)

for p in permutation(result):
    print(p)
