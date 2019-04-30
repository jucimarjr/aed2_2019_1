def fatorial (x):
    if (x == 0):
        return 1
    else:
        return (x * (fatorial (x-1)))

def combinacao(m,n):
    return (fatorial(m))/((fatorial(m-n))*fatorial(n))

def imprime(m, n):
    for i in range(m):
        print(i)
        for j in range(n):
            print 


    

#num = int(input())
#num = int(num)

x = int(input())
y = int(input())

print (combinacao(x, y))
print (imprime(x, y))