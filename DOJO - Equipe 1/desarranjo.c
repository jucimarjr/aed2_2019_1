//Algoritmo de Desarranjo ou permutação caotica

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void desarranjo(int posicao, char *entrada, int *visitados, char *resposta, int n){ //recebe uma posição, o vetor de entrada, o vetor de visitados, vetor de respostas e o tamanho do vetor

    if(posicao == n){ //se a posicação for igual ao tamanho do vetor de entrada significa que ele terminou e imprime a resposta
        for(int i=0;i<n;i++){
            printf("%c ",resposta[i]);
        }
        printf("\n");
    }
    for(int i=0;i<n;i++){
        if((i != posicao) && (visitados[i]==0)){  //o vetor de visitados marca quais ele ja passou
            visitados[i] = 1;
            resposta[posicao] = entrada[i];
            desarranjo(posicao+1, entrada, visitados, resposta, n); //chamada recursiva para a proxima posicação do vetor
            visitados[i] = 0;
        }
    }
}


int main(){
    char entrada[] = {'1','2','3','4'}; //recebe um valor de entrada
    int n = sizeof(entrada)/sizeof(char); //armazena o tamanho do vetor
    int *visitados; 
    char *resposta; 
    visitados = malloc(n * sizeof(int)); //aloca dinamicamente o tamanho do vetor
    resposta = malloc(n * sizeof(char)); //aloca dinamicamente o tamanho do vetor

    memset(visitados,0,sizeof(visitados)); //seta para 0 todas as posições do vetor

    desarranjo(0, entrada, visitados, resposta, n); //passa-se como parametros para a função: 0, como posição inicial, um vetor de entrada, um de visitado,um de resposta r o tamanho do vetor

    free(visitados);
    free(resposta);
    return 0;
}
