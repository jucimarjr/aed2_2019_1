#include "io.h"
// a função não segue fielmente o padrão para manter
// propriedade recursiva
void quick_sort(int vector[], int beginning, int end)
{
	int i, j, pivot, aux;
	i = beginning;
	j = end - 1;
	pivot = vector[(beginning + end) / 2];

	while(i <= j)
	{
		while(vector[i] < pivot && i < end)
		{
			i++;
		}

		while(vector[j] > pivot && j > beginning)
		{
			j--;
		}

		if(i <= j)
		{
			aux = vector[i];
			vector[i] = vector[j];
			vector[j] = aux;
			i++;
			j--;

		}

	}

	if(j > beginning)
		quick_sort(vector, beginning, j+1);
	if(i < end)
		quick_sort(vector, i, end);
}

int main()
{
    int vector[1000];
		read(vector);
		quick_sort(vector, 0, 1000);
		print(vector);

    return 0;
}
