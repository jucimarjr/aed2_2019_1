#include "io.h"

void insertion_sort(int vector[])
{
	int i, key, j;
	for (i = 1; i < TAM; i++)
  	{
		key = vector[i];
		j = i - 1;
		while (j >= 0 && vector[j] > key)
		{
			vector[j + 1] = vector[j];
			j = j - 1;
		}
		vector[j + 1] = key;
	}
}

int main()
{
	int vector[TAM];
	read(vector);
	insertion_sort(vector);
	print(vector);

	return 0;
}
