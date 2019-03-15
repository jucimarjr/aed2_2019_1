#include "io.h"
// #include <stdlib.h>

void heapfy(int vect[], int size, int i)
{
    int exchange;
    int biggest = i;
    int left = i*2 + 1;
    int right = i*2 + 2;

    if(left < size && vect[left] > vect[biggest])
	{
        biggest = left;
    }

    if(right < size && vect[right] > vect[biggest])
	{
        biggest = right;
    }

    if(biggest != i)
	{
        exchange = vect[i];
        vect[i] = vect[biggest];
        vect[biggest] = exchange;

        heapfy(vect, size, biggest);
    }
}

void heap_sort(int vect[],int size)
{

    int temp;

    for(int i = (size/2) - 1 ; i >= 0 ; i-- )
	{
        heapfy(vect, size, i);

    }


    for(int i = size - 1 ; i >= 0 ; i--)
	{
        temp = vect[0];
        vect[0] = vect[i];
        vect[i] = temp;

        heapfy(vect, i, 0);
    }

}
/*
int main()
{    
  int vector[1000];

  read(vector, 1000);
  heap_sort(vector, 1000);
  print(vector, 1000);

    return 0;
}
*/
