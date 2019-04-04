#include <stdlib.h>
#include <stdio.h>

void swap(int vetor[],int x, int y)
{ 
    int aux = vetor[x]; 
    vetor[x] = vetor[y]; 
    vetor[y] = aux; 
} 
/*
int parent(int vetor[], int pos)
{
    return vetor[pos/2];
}
int left(int vetor[], int pos)
{
    return vetor[2*pos];
}
int right(int vetor[], int pos)
{
    return vetor[2*pos + 1];
}
*/
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
void create_max_heap(int* heap_size, int vetor[])
{

    for(int i = (*heap_size/2) ; i >= 1 ;i-- )
	{
        heapfy(vetor, *heap_size, i);
    }

}


int insert(int* heap_size, int vetor[], int insercao)
{
    vetor[*heap_size] = insercao;

    (*heap_size)++;
    
    for(int i = (*heap_size/2) ; i >= 1 ;i-- )
	{
        heapfy(vetor, *heap_size, i);
    }

}

void extract_max(int vetor[], int* heap_size)
{

    swap(vetor, 1, *heap_size-1);

    heapfy(vetor, *heap_size-1, 1);

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

    int vetor[] = {0, 1, 5, 3, 3, 2, 10};
    int heap_size = (sizeof(vetor)/sizeof(int));

    create_max_heap(&heap_size, vetor);

    extract_max(vetor, &heap_size);

    insert(&heap_size, vetor, 10);

    heap_sort(vetor, &heap_size);

    for(int i=1; i< heap_size; i++) printf("%d ", vetor[i]);


    return 0;

}