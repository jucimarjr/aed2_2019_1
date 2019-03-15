#include "io.h"
#include <stdlib.h>

void merge(int vector[], int beginning, int middle, int end)
{
    int com1 = beginning, com2 = middle+1, com_aux = 0, size = end-beginning+1;
    int *vect_aux;
    vect_aux = (int*)malloc(size * sizeof(int));

    while(com1 <= middle && com2 <= end-1)
	{
        if(vector[com1] < vector[com2])
		{
            vect_aux[com_aux] = vector[com1];
            com1++;
        }
		else
		{
            vect_aux[com_aux] = vector[com2];
            com2++;
        }
        com_aux++;
    }

    while(com1 <= middle)
	{
        vect_aux[com_aux] = vector[com1];
        com_aux++;
        com1++;
    }

    while(com2 <= end)
	{
        vect_aux[com_aux] = vector[com2];
        com_aux++;
        com2++;
    }

    for(com_aux = beginning; com_aux <= end; com_aux++)
	{
        vector[com_aux] = vect_aux[com_aux-beginning];
    }

    free(vect_aux);
}

void merge_sort(int vector[], int beginning, int end)
{
    if (beginning < end)
	{
        int middle = (end+beginning)/2;

        merge_sort(vector, beginning, middle);
        merge_sort(vector, middle + 1, end);
        merge(vector, beginning, middle, end);
    }
}

/* int main()
{
    int vector[1000];

    read(vector, 1000);
    merge_sort(vector, 0, 1000);
    print(vector, 1000);
    return 0;
} */
