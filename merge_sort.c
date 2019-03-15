#include "io.h"
#include <stdlib.h>

void merge(int vector[], int beginning, int middle, int end) {

    int beginning1 = beginning;
    int beginning2 = middle + 1;
    int beginningAux = 0;
    int tam = end - beginning + 1;
    int *vetAux;

    vetAux = (int*)malloc(tam * sizeof(int));

    while(beginning1 <= middle && beginning2 <= end)
    {
        if(vector[beginning1] < vector[beginning2])
        {
            vetAux[beginningAux] = vector[beginning1];
            beginning1++;

        }
        else
        {
            vetAux[beginningAux] = vector[beginning2];
            beginning2++;

        }
        beginningAux++;
    }

    while(beginning1 <= middle)
    {
        vetAux[beginningAux] = vector[beginning1];
        beginningAux++;
        beginning1++;

    }


    while(beginning2 <= end)
    {
        vetAux[beginningAux] = vector[beginning2];
        beginningAux++;
        beginning2++;

    }


    for(beginningAux = beginning; beginningAux <= end; beginningAux++)
    {
        vector[beginningAux] = vetAux[beginningAux-beginning];
    }

    free(vetAux);

}

void merge_sort(int vector[], int beginning, int end)
{
    if (beginning < end) {
        int middle = (end+beginning)/2;
        merge_sort(vector, beginning, middle);
        merge_sort(vector, middle+1, end);
        merge(vector, beginning, middle, end);

    }

}

int main()
{
    int vector[1000];
    read(vector);
    merge_sort(vector, 0, TAM);
    print(vector);

    return 0;
}
