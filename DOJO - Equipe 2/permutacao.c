#include <stdio.h>
#include <stdlib.h>

//função que irá trocar os elementos do vetor
void troca(int vetor[], int i, int j){
	int aux;
	aux=vetor[i];
	vetor[i]=vetor[j];
	vetor[j]=aux;
}


//a função que permuta de fato
void permutacao(int vetor[], int k, int n) {
	//aqui ele só irá imprimir quando o valor de k chegar ao valor do tamanho do vetor
	if(k == n){
		printf("(");
		for(int i=0;i<n;i++){
			printf("%d", vetor[i]);
		}
		printf(")");
		printf(" ");
	//aqui ele é onde ele permuta entre os proprios valores do vetor, onde eu chamo a função de trocar e chamo recursivamente a função de permutação onde ele incrementa a variavel de k
	} else {
		for(int i=k;i<n;i++){
			troca(vetor,k,i);
			permutacao(vetor, k+1, n);
			troca(vetor,k,i);
		}
	}
}

//função básica pra organizar a chamada na função principaç
void listar_permutacao(int vetor[], int n){
	permutacao(vetor, 0, n);
}

int main() {
	int *vetor, n;
	printf("Digite o tamanho do vetor: ");
	scanf("%d", &n);
	vetor = (int *)malloc(n * sizeof(int));
	for(int i = 0; i < n; i++){
		printf("Posicao %d: ", i+1);
		scanf("%d", &vetor[i]);
	}
	listar_permutacao(vetor, n);
	free(vetor);
	return 0;
}
