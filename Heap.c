#include <stdlib.h>
#include <stdio.h>
#include "io.h"

#define TAM 1000

void swap(int vector[],int x, int y)
{ 
    int aux = vector[x]; 
    vector[x] = vector[y]; 
    vector[y] = aux; 
} 

int heapfy(int vector[], int size, int i)
{
    int exchange;
    int biggest = i;
    int left = i*2;
    int right = i*2 + 1;

    if(left < size && vector[left] > vector[biggest])
	{
        biggest = left;
    }

    if(right < size && vector[right] > vector[biggest])
	{
        biggest = right;
    }

    if(biggest != i)
	{
        exchange = vector[i];
        vector[i] = vector[biggest];
        vector[biggest] = exchange;

        heapfy(vector, size, biggest);
    }
}

void create_max_heap(int* heap_size, int vector[])
{

    for(int i = (*heap_size/2) ; i >= 1 ;i-- )
	{
        heapfy(vector, *heap_size, i);
    }

}

int insert(int* heap_size, int vector[], int insercao)
{
    vector[*heap_size] = insercao;

    (*heap_size)++;
    
    for(int i = (*heap_size/2) ; i >= 1 ;i-- )
	{
        heapfy(vector, *heap_size, i);
    }

}

void extract_max(int vector[], int* heap_size)
{

    swap(vector, 1, *heap_size-1);

    heapfy(vector, *heap_size-1, 1);

    (*heap_size)--;

}

void heap_sort(int vector[], int* heap_size)
{

    int temp;

    for(int i = (*heap_size/2) - 1 ; i >= 0 ; i-- )
	{
        heapfy(vector, *heap_size, i);

    }


    for(int i = *heap_size - 1 ; i >= 0 ; i--)
	{
        temp = vector[0];
        vector[0] = vector[i];
        vector[i] = temp;

        heapfy(vector, i, 0);
    }

}

int main()
{

    int vector[TAM];
    int heap_size = (sizeof(vector)/sizeof(int));
    read(vector);
    create_max_heap(&heap_size, vector);

    extract_max(vector, &heap_size);

    insert(&heap_size, vector, 10);

    heap_sort(vector, &heap_size);

    print(vector);


    return 0;

}
