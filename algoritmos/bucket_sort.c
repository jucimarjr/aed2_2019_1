#include <stdio.h>
#include <stdlib.h>

#include "../print.h"
#include "../read.h"

struct bucket;

int compare_integers(const void* first, const void* second);
void bucket_sort(int array[],int n);

int main() 
{
	
	FILE *arq;
	int array[1000]; // Considerando que o espaco do vetor seja infinito
	int v_size;
	
	v_size = read_vector(arq, "../teste.txt", array, v_size);
	
	bucket_sort(array,v_size);// Insere aqui o algoritmo de ordenacao
	
	print_vector(array, v_size);
	
	return 0;
}

struct bucket 
{
    int count;
    int* value;
};
 
int compare_integers(const void* first, const void* second)
{
    int x = *((int*)first), y =  *((int*)second);
    if (x == y)
    {
        return 0;
    }
    else if (x < y)
    {
        return -1;
    }
    else
    {
        return 1;
    }
}
 
void bucket_sort(int array[],int n)
{
    struct bucket buckets[3];
    int i, j, k;
    for (i = 0; i < 3; i++)
    {
        buckets[i].count = 0;
        buckets[i].value = (int*)malloc(sizeof(int) * n);
    }
    
    for (i = 0; i < n; i++)
    {
        if (array[i] < 0)
        {
            buckets[0].value[buckets[0].count++] = array[i];
        }
        else if (array[i] > 10)
        {
            buckets[2].value[buckets[2].count++] = array[i];
        }
        else
        {
            buckets[1].value[buckets[1].count++] = array[i];
        }
    }
    for (k = 0, i = 0; i < 3; i++)
    {
        qsort(buckets[i].value, buckets[i].count, sizeof(int), &compare_integers);
        for (j = 0; j < buckets[i].count; j++)
        {
            array[k + j] = buckets[i].value[j];
        }
        k += buckets[i].count;
        free(buckets[i].value);
    }
}
