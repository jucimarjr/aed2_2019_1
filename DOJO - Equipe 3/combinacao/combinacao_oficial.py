
def combinacao(vetor, n, vetor0 = []):
    if n == 1:
        for i in range(len(vetor)):
            print(vetor0 + [vetor[i]])
    else:
        for i in range(len(vetor)-n+1):
            combinacao(vetor[i+1:], n-1, vetor0+[vetor[i]])

combinacao([1,2,3,4,5,6,7,8,9,10], 4)