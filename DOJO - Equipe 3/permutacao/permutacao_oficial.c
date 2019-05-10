#include <stdio.h>
#include <stdlib.h>

void permutacao(int array[], int k, int n) {
	int i;
	if(k == n){
		printf("(");
		for(i=0;i<n;i++){
			printf(" %d", array[i]);
		}
		printf(")");
		printf(" ");
	} else {
		for(i=k;i<n;i++){
			troca(array,k,i);
			permutacao(array, k+1, n);
			troca(array,k,i);
		}
	}
}

void troca(int array[], int i, int j){
	int aux;
	aux=array[i];
	array[i]=array[j];
	array[j]=aux;
}

int main() {
	int *array, n, i;
	printf("Digite o tamanho do array: ");
	scanf("%d", &n);
	array = (int *)malloc(n * sizeof(int));
	for(i = 0; i < n; i++){
		printf("Posicao %d: ", i+1);
		scanf("%d", &array[i]);
	}
	permutacao(array, 0, n);
	free(array);
	return 0;
}
