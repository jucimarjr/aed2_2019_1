#include "io.h"
void quick_sort(int vect[], int beginning, int end)
{
	int i, j, pivot, aux;
	i = beginning;
	j = end-1;
	pivot = vect[(beginning + end) / 2];
	while(i <= j)
	{
		while(vect[i] < pivot && i < end)
		{
			i++;
		}
		while(vect[j] > pivot && j > beginning)
		{
			j--;
		}
		if(i <= j)
		{
			aux = vect[i];
			vect[i] = vect[j];
			vect[j] = aux;
			i++;
			j--;
		}
	}
	if(j > beginning)
		quick_sort(vect, beginning, j+1);
	if(i < end)
		quick_sort(vect, i, end);
}

/*
int main()
{

    int vector[1000];

		read(vector, 1000);

		quick_sort(vector, 0, 1000);

		print(vector, 1000);


    return 0;
}
*/
