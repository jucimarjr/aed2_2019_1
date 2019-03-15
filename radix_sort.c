#include <stdio.h>
#include "io.h"

void radix_sort(int vector[]) {
    int i, b[TAM], m = 0,  exp = 1;
    for (i = 0; i < TAM;  i++) 
    {
        if (vector[i] > m)
        m = vector[i];
    }

    while (m / exp >  0) {
    int box[TAM] = { 0 };
    for (i = 0; i <  TAM; i++)
        box[vector[i] / exp %  TAM]++;
    for (i = 1; i <  TAM; i++)
        box[i] += box[i -  1];
    for (i = TAM - 1; i  >= 0; i--)
        b[--box[vector[i] / exp  % TAM]] = vector[i];
    for (i = 0; i <  TAM; i++)
        vector[i] = b[i];
    exp *= TAM;
    }
}

int main()
{
    int vector[TAM];
    read(vector);
    radix_sort(vector);
    print(vector);

    return 0;
}
