#include <stdio.h>
#include <stdlib.h>

// Movimentos do cavalo
int movimX[8] = {  2, 1, -1, -2, -2, -1,  1,  2 }; 
int movimY[8] = {  1, 2,  2,  1, -1, -2, -2, -1 }; 

typedef struct coordenada_t{
	int x, y;
} coordenada_t;

int rotaCavalo_real(int n, int **tabuleiro, coordenada_t *rota, int *passo);
int rotaCavalo(int n);

int main(int argc, char **argv){
	int n;
	printf("Digite a ordem (n) do tabuleiro (que tem n x n casas): ");
	scanf("%d", &n);
	printf("\n");
	
	rotaCavalo(n);
	return 0;
}

int rotaCavalo(int n){
	int i, j, passo, ret;
	int **tabuleiro = (int**) malloc(n * sizeof(int*));
	for(i = 0; i < n; i++){
		tabuleiro[i] = malloc(n * sizeof(int));
		for(j = 0; j < n; j++){
			tabuleiro[i][j] = -1;
		}
	}
	coordenada_t *rota = malloc(n * sizeof(coordenada_t));
	rota[0].x = 0;
	rota[0].y = 0;
	tabuleiro[0][0] = 0;
	passo = 1;
	ret = rotaCavalo_real(n, tabuleiro, rota, &passo);
	if(ret == 1){
		for(i = 0; i < n; i++){
			for(j = 0; j < n; j++){
				printf("%d ", tabuleiro[i][j]);
			}
			printf("\n");
		}
		printf("\n\nRota: (%d, %d)", rota[0].x, rota[0].y);
		for(i = 1; i < (n*n); i++){
			printf("  ->  (%d, %d)", rota[i].x, rota[i].y);
		}
		printf("\n");
	}1
	return ret;
}

int rotaCavalo_real(int n, int **tabuleiro, coordenada_t *rota, int *passo){
	int i;
	coordenada_t novoLocal;
	if((*passo) == (n*n)){
		return 1;
	}
	for(i = 0; i < 8; i++){
		novoLocal.x = rota[(*passo)-1].x + movimX[i];
		novoLocal.y = rota[(*passo)-1].y + movimY[i];
		if((novoLocal.x < 0) || (novoLocal.x >= n) || (novoLocal.y < 0) || 
		   (novoLocal.x < 0) || (tabuleiro[novoLocal.x][novoLocal.y] != -1)){
				continue;
		}
		tabuleiro[novoLocal.x][novoLocal.y] = (*passo);
		rota[*passo] = novoLocal;
		(*passo)++;
		if(rotaCavalo_real(n, tabuleiro, rota, passo) == 1){
			return 1;
		}
		else{
			// Backtracking: volta ao estado anterior
			tabuleiro[novoLocal.x][novoLocal.y] = -1;
			(*passo)--;
		}
	}
	return 0;
}
