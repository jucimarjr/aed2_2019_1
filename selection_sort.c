#include io.h

int selection_sort(int *vector, int size){
    int smallest;
    int aux;
    int aux_vect[size] = vector;

    for( int i = 0; i < size-1; i++)
    {
        smallest = i;

        for (int j = i+1; j < size; j++)
        {
            if (aux_vect[j] < aux_vect[smallest])
            {
                smallest = j;
            }
        }
        aux = aux_vect[i];
        aux_vect[i] = aux_vect[smallest];
        aux_vect[smallest] = aux;

    }
    return aux_vect;
}

int main()
{
	int vector[TAM];
	int result[TAM];
	create_vector(vector, TAM);
	result = selection_sort(vector, TAM);
	print_vector(result, TAM);
	return 0;
}
