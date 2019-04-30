def permutacao(m, k): 
	n = len(m) 
	imprime(m, "", n, k) 

def imprime(m, prefix, n, k): 
	if (k == 0) : 
		print(prefix) 
		return
	for i in range(n): 
		newPrefix = prefix + m[i] 
		imprime(m, newPrefix, n, k - 1) 
 
set2 = ['1', '2', '3', '4'] 
k = 3
permutacao(set2, k) 