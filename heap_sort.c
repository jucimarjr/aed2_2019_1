#include "io.h"

void heapfy(int vector[], int size, int i)
{
    int exchange;
    int biggest = i;
    int left = i*2 + 1;
    int right = i*2 + 2;

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

void heap_sort(int vector[])
{

    int temp;

    for(int i = (TAM/2) - 1 ; i >= 0 ; i-- )
	{
        heapfy(vector, TAM, i);

    }


    for(int i = TAM - 1 ; i >= 0 ; i--)
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
  read(vector);
  heap_sort(vector);
  print(vector);

  return 0;
}
