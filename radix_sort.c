#include <stdio.h>
#include "io.h"

void radix_sort(int numbers[], int size)
{
    int i;
    int *b;
    int max = numbers[0];
    int count = 1;

    b = (int *)calloc(size, sizeof(int));

    for (i = 0; i < size; i++)
	{
        if (numbers[i] > max)
    	    max = numbers[i];
    }

    while (max/count > 0)
	{
        int bucket[10] = { 0 };
    	for (i = 0; i < size; i++)
    	    bucket[(numbers[i] / count) % 10]++;
    	for (i = 1; i < 10; i++)
    	    bucket[i] += bucket[i - 1];
    	for (i = size - 1; i >= 0; i--)
    	    b[--bucket[(numbers[i] / count) % 10]] = vetor[i];
    	for (i = 0; i < size; i++)
    	    numbers[i] = b[i];
    	count *= 10;
    }

    free(b);
}