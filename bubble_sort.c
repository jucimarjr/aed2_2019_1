#include "io.h"

void bubble_sort(int numbers[], int size)
{
	int aux;
	for(int counter = 1 ; counter < size ; counter++)
	{
		for(int i = 0 ; i < size -1 ; i++)
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
/*
int main()
{
	int vector[TAM];
	create_vector(vector, TAM);
	bubble_sort(vector, TAM);
	print_vector(vector, TAM);
	return 0;
}
*/
