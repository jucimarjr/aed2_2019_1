/******************************************************************************
AED2
Andressa Carla Pinheiro Moreira 0525060103
Combinação em c: exibir as subsequências que têm exatos k termos.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int main(){
   int *vet;
   int k, n, i, j, m;
   
   printf("Quantos numeros serao inseridos: ");
   scanf("%d", &n);
   //alocação dinâmica pra criação do vetor
   vet = (int *) malloc (n*sizeof(int));
   //cria vetor de 0 a n-1
   for(i = 0; i < n; i++){
       printf("Preencha a posicao %d do vetor: ", i);
       scanf("%d", &vet[i]);
   }
   
   printf("Informe o valor de k: ");
   scanf("%d", &k);
   
   /*Combinação: percorre o vetor, pega o valor da posição, 
   verifica se j é menor que o tamanho do vetor e imprime o valor.
   Busca o próximo valor e imprime até que m chegue a j.*/
   
   for(i = 0; i < n; i++){
       for(j = i+1; j < n-(k-2); j++){
           printf("%d", vet[i]);
           for(m = j; m < j+k-1; m++){
               printf(",%d", vet[m]);
           }
           printf("\n");
       }
   }
   
    return 0;
}
