def Desarranjo(entrada):
    lista = entrada
    saida = []
    troca = 0
    for i in range(len(lista)):
        cont = 1
        while(cont <= len(lista)-2):
            if (troca == len(lista) - 1):
                troca = 0 
            aux = lista[troca]
            lista[troca] = lista[troca+1]
            lista[troca+1]=aux
            cont+=1
            troca+=1
        print(lista, "\n")
    
    return saida 

Desarranjo([1,2,3])
        
        
