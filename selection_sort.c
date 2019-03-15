#include "io.h"

int selection_sort(int vector[])
{
    int smallest;
    int aux;
    
    for( int i = 0; i < TAM-1; i++)
    {
        smallest = i;

        for (int j = i+1; j < TAM; j++)
        {
            if (vector[j] < vector[smallest])
            {
                smallest = j;
            }
        }
        aux = vector[i];
        vector[i] = vector[smallest];
        vector[smallest] = aux;

    }
    
}

int main()
{
	int vector[TAM];
	read(vector);
	selection_sort(vector);
	print(vector);
	return 0;
}

