#include <stdio.h>
#include <stdlib.h>


void permutation(int vector[], int k, int n) {
	
	if(k == n){
		printf("(");
		for(int i=0;i<n;i++){
			printf("%d", vector[i]);
		}
		printf(")");
		printf(" ");
	} else {
		for(int i=k;i<n;i++){
			exchange(vector,k,i);
			permutation(vector, k+1, n);
			exchange(vector,k,i);
		}
	}
}


void exchange(int vector[], int i, int j){
	int aux;
	aux=vector[i];
	vector[i]=vector[j];
	vector[j]=aux;
}



void ListPermutation(int vector[], int n){
	permutation(vector, 0, n);
}

int main() {
	int *vector, n;
	printf("type the vector size ");
	scanf("%d", &n);
	vector = (int *)malloc(n * sizeof(int));
	for(int i = 0; i < n; i++){
		printf("position %d: ", i+1);
		scanf("%d", &vector[i]);
	}
	ListPermutation(vector, n);
	free(vector);
	return 0;
}
