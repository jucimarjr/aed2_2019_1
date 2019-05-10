// C program for Knight Tour problem
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>



int solucaoAte(int N, int x, int y, int movei, int sol[N][N],
                int xMove[], int yMove[]);


bool Seguro(int N, int x, int y, int sol[N][N])
{
    return ( x >= 0 && x < N && y >= 0 &&
             y < N && sol[x][y] == -1);
}

void printSolution(int N, int sol[N][N], FILE* ofp)
{
    for (int x = 0; x < N; x++)
    {
        for (int y = 0; y < N; y++)

            fprintf (ofp, " %2d ", sol[x][y]);
            //printf(" %2d ", sol[x][y]);

        fprintf(ofp, "\n");
        //printf("\n");
    }
}

bool solucao(int N, FILE* ofp)
{
    int sol[N][N];

    /* Inicializaacao da matriz */
    for (int x = 0; x < N; x++)
        for (int y = 0; y < N; y++)
            sol[x][y] = -1;

    /* xMove[] e yMove[] Sao os movimentos do cavalo.*/

    int xMove[8] = {  2, 1, -1, -2, -2, -1,  1,  2 };
    int yMove[8] = {  1, 2,  2,  1, -1, -2, -2, -1 };

    // Comecar do primeiro bloco e a partir dai explorar tudo
    sol[0][0]  = 0;


    if (solucaoAte(N, 0, 0, 1, sol, xMove, yMove) == false)
    {
        printf("Solution does not exist");
        return false;
    }
    else
        printSolution(N, sol, ofp);

    return true;
}

/* A recursive utility function to solve Knight Tour
   problem */
int solucaoAte(int N, int x, int y, int movei, int sol[N][N],
                int xMove[N], int yMove[N])
{
   int k, next_x, next_y;
   if (movei == N*N)
       return true;

   /* Try all next moves from the current coordinate x, y */
   for (k = 0; k < 8; k++)
   {
       next_x = x + xMove[k];
       next_y = y + yMove[k];
       if (Seguro(N, next_x, next_y, sol))
       {
         sol[next_x][next_y] = movei;
         if (solucaoAte(N, next_x, next_y, movei+1, sol,
                         xMove, yMove) == true)
             return true;
         else
             sol[next_x][next_y] = -1;// backtracking
       }
   }

   return false;
}
/* Driver program to test above functions */
int main()
{
    FILE *ifp, *ofp;
	ifp = fopen("Entrada5.txt", "r");
    ofp = fopen("Saida5.txt", "w");

    int n;
    fscanf(ifp, "%d", &n);

	solucao(n, ofp);

    fclose(ofp);
	fclose(ifp);
	return 0;
}
