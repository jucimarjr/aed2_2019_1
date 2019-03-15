#include "io.h"
#include <stdlib.h> 
  
/*  Counting sort function  */

int max_element(int vector[])
{
    int max = 0, i;

    for (i = 0; i < TAM; i++)
    {
        if (max < vector[i])
            max = vector[i];
    }
    return max;
}

int  counting_sort(int vector[])
{
    int i, j, k = max_element(vector);
    int b[TAM], c[TAM];
    for (i = 0; i <= k; i++)
        c[i] = 0;
    for (j = 1; j <= TAM; j++)
        c[vector[j]] = c[vector[j]] + 1;
    for (i = 1; i <= k; i++)
        c[i] = c[i] + c[i-1];
    for (j = TAM; j >= 1; j--)
    {
        b[c[vector[j]]] = vector[j];
        c[vector[j]] = c[vector[j]] - 1;
    }
    for (i = 1; i <= TAM; i++){
        vector[i] = b[i];
    }
}

int  main()
{
    int vector[TAM];
    read(vector);
    counting_sort(vector);
    print(vector);

    return 0;
}
