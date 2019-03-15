#include "io.h"

void bubble_sort(int vector[])
{
	int aux;
	for(int counter = 1 ; counter < TAM ; counter++)
	{
		for(int i = 0 ; i < TAM -1 ; i++)
		{
			if(vector[i] > vector[i+1])
			{
				aux = vector[i];
				vector[i] = vector[i+1];
				vector[i+1] = aux;
			}
		}
	}
}

int main()
{
	int vector[TAM];
  	read(vector);
	bubble_sort(vector);
	print(vector);

	return 0;
}
