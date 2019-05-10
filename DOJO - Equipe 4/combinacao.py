def Combination(list, number):
    a = number
    output = []
    combination = []
     
    for i in range(len(list) - (a-1)):
        
        sentinel = list[i]
        
        for j in range((i),(len(list)-(a-1))):
            
            combination.append(sentinel)
            cont = 1
           
            while (cont < number):
                
                combination.append(list[j+cont])
                cont+=1
            
            output.append(combination)
            
            combination=[]
    
    return output

for i in Combination([1,2,3,4,5,6,7], 4):
    print(i)


