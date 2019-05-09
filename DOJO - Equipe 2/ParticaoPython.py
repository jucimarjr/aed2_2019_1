def particoes(A):
	if not A: #verifica se a lista A esta vazia
		yield []
	else:
		a, *R = A # 'a' recebe o conteudo da primeira posicao da lista e 'b' recebe o resto do conteudo
		for particao in particoes(R): #inicia a recursao
			yield particao + [[a]]
			for i, subset in enumerate(particao): #enumera cada item da lista retornada 
				yield particao[:i] + [subset + [a]] + particao[i+1:] #retorna a particao naquele momento

if __name__ == '__main__':
	vet = {1,2,3,4}
	for particao in particoes(vet):
		print(particao)