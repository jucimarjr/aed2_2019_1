#include "io.h"
#include <stdlib.h>


struct bucket
{
    int count;
    int* value;
};

int compare_integers(const void* first, const void* second)
{
    int x = *((int*)first), y =  *((int*)second);
    if (x == y)
    {
        return 0;
    }
    else if (x < y)
    {
        return -1;
    }
    else
    {
        return 1;
    }
}

void bucket_sort(int vector[])
{
    struct bucket buckets[3];
    int i, j, k;
    for (i = 0; i < 3; i++)
    {
        buckets[i].count = 0;
        buckets[i].value = (int*)malloc(sizeof(int) * TAM);
    }

    for (i = 0; i < TAM; i++)
    {
        if (vector[i] < 0)
        {
            buckets[0].value[buckets[0].count++] = vector[i];
        }
        else if (vector[i] > 10)
        {
            buckets[2].value[buckets[2].count++] = vector[i];
        }
        else
        {
            buckets[1].value[buckets[1].count++] = vector[i];
        }
    }
    for (k = 0, i = 0; i < 3; i++)
    {
        qsort(buckets[i].value, buckets[i].count, sizeof(int), &compare_integers);
        for (j = 0; j < buckets[i].count; j++)
        {
            vector[k + j] = buckets[i].value[j];
        }
        k += buckets[i].count;
        free(buckets[i].value);
    }
}

int main()
{
    int vector[TAM];
    read(vector);
    bucket_sort(vector);
    print(vector);

    return 0;
}

