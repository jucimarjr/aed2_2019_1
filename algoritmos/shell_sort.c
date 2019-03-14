#include <stdio.h>
#include <stdlib.h>

#include "../print.h"
#include "../read.h"

void shell_sort(int *a, int size);

int main()
{
	
	FILE *arq;
	int array[1000]; // Considerando que o espaco do vetor seja infinito
	int v_size;
	
	v_size = read_vector(arq, "../teste.txt", array, v_size);
	
	shell_sort(array, v_size); // Insere aqui o algoritmo de ordenacao
	
	print_vector(array, v_size);
	
	return 0;
}

void shell_sort(int *a, int size)
{
	int i , j , value;
	int gap = 1;

	do 
	{
		gap = 3*gap+1;
	} while(gap < size);

	do 
	{
		gap /= 3;
		for(i = gap; i < size; i++) 
		{
			value = a[i];
			j = i - gap;

			while (j >= 0 && value < a[j])
			{
				a[j + gap] = a[j];
				j -= gap;
			}

			a[j + gap] = value;
		}
	}while(gap > 1);
}
