#include "io.h"
#define TAM 1000

int bubble_sort(int vector[])
{
	int aux;
	int vector_aux[TAM] = vector[];
	for(int counter = 1 ; counter < TAM ; counter++)
	{
		for(int i = 0 ; i < TAM -1 ; i++)
		{
			if(vector_aux[i] > vector_aux[i+1])
			{
				aux = vector_aux[i];
				vector_aux[i] = vector_aux[i+1];
				vector_aux[i+1] = aux;
			}
		}
	}
    return vector_aux;
}

int main()
{
   	int vector[TAM];
   	int result[TAM];

   	vector = read(vector);
	result = bubble_sort(vector);
	print(result);

	return 0;
}
