#include "io.h"


void insertion_sort(int arr[], int size)
{
	int i, key, j;
	int * vet_aux = arr;
	for (i = 1; i < size; i++)
  {
		key = vet_aux[i];
		j = i - 1;

		while (j >= 0 && vet_aux[j] > key)
		{
			vet_aux[j + 1] = vet_aux[j];
			j = j - 1;
		}
		vet_aux[j + 1] = key;
	}
	arr = vet_aux;
}

/*
int main()
{
	int vector[TAM];
	read(vector, TAM);
	insertion_sort(vector, TAM);
	print(vector, TAM);


	return 0;

}
 */ 
