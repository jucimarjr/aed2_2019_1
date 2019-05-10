def  desarranjo(entrada):
    vetor=[]
    vetor_principal=[]
    for i in range(len(entrada)):
        x=i
        if i != 0:
            for y in range(len(entrada)):
                vetor.append(entrada[x])
                x+=1
                if(x==len(entrada)):
                    x=0
            vetor_principal.append(vetor)
            vetor=[]
    return vetor_principal

saida=desarranjo([1,2,3,4,5,6,7,8,9,10])
print(saida)
