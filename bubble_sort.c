#include "io.h"

void bubble_sort(int numbers[])
{
	int aux;
	for(int counter = 1 ; counter < TAM ; counter++)
	{
		for(int i = 0 ; i < TAM -1 ; i++)
		{
			if(numbers[i] > numbers[i+1])
			{
				aux = numbers[i];
				numbers[i] = numbers[i+1];
				numbers[i+1] = aux;
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
