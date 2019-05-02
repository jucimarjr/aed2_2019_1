def Desarranjo(listaOriginal):
    lista = listaOriginal
    combinacoes = []
    swap = 0
    for i in range(len(lista)):
        cont = 1
        while(cont <= len(lista)-2):
            if (swap == len(lista) - 1):
                swap = 0 
            aux = lista[swap]
            lista[swap] = lista[swap+1]
            lista[swap+1]=aux
            cont+=1
            swap+=1
        print(lista, "\n")
    
    return combinacoes 

Desarranjo([1,2,3])
        
        