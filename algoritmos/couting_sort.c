#include <stdio.h>
#include <stdlib.h>

#include "../print.h"
#include "../read.h"
 
void counting_sort(int a[],int n)
{
    int count[50]={0},i,j,cont=0;

    for(i=0;i<n;++i)
        count[a[i]]=count[a[i]]+1;

    max = get_max_value(array, v_size);

    for(i=0;i<=max;++i)
        for(j=1;j<=count[i];++j)
        {
            new_array[cont] = i;
            cont++;
        }

    return new_array
}

void get_max_value(int array[], int v_size)
{

    int i, max = 0;

    for(i=0;i<v_size;++i)
    {
        if(array[i]>max)
            max=array[i];
    }

    return max

}
 
int main()
{

    FILE *arq;
    int array[1000]; // Considerando que o espaco do vetor seja infinito
    int v_size;
    
    v_size = read_vector(arq, "../teste.txt", array, v_size);
    
    array = counting_sort(array,v_size); // Insere aqui o algoritmo de ordenacao
    
    print_vector(array, v_size);
    
    return 0;
}
