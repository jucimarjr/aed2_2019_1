#include <stdlib.h>
#include "io.h"

void swap(int vector[],int x, int y) // change values between two given positions in the vector
{ 
    int aux = vector[x]; 
    vector[x] = vector[y]; 
    vector[y] = aux; 
} 

int heapfy(int vector[], int size, int i ) // compares the values in a sub-tree (a parent and its two children) and applies the heap property
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

void create_max_heap(int* heap_size, int vector[]) // apply the maximum heap property that says that the parent should be bigger than its children
{

    for(int i = (*heap_size/2) ; i >= 1 ;i-- )
	{
        heapfy(vector, *heap_size, i);
    }

}

int insert(int* heap_size, int vector[], int insercao) // insert an element on the vector
{
    vector[*heap_size] = insercao;

    (*heap_size)++;
    
    for(int i = (*heap_size/2) ; i >= 1 ;i-- )
	{
        heapfy(vector, *heap_size, i);
    }

}

void extract_max(int vector[], int* heap_size) // it extracts the element that is stored in the root of the binary heap tree
{

    swap(vector, 1, *heap_size-1);

    heapfy(vector, *heap_size-1, 1);

    (*heap_size)--;

}

void heap_sort(int vector[], int* heap_size) // a sorting algorithm based on heap properties
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
