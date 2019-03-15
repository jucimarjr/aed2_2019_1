#include "io.h"

void shell_sort(int *a, int size);

void shell_sort(int *vector, int size)
{
 int i, j, value;
 int gap = 1;

 do
 {
   gap = 3 * gap + 1;
 }while(gap < size);

 do
 {
   gap /= 3;
   for(i = gap; i < size; i++)
   {
     value = vector[i];
     j = i - gap;

     while (j >= 0 && value < vector[j])
     {
       vector[j + gap] = vector[j];
       j -= gap;
     }

     vector[j + gap] = value;
  }
 }while(gap > 1);
}
/*
int main()
{
  int vector[TAM];
  read(vector, TAM);
  shell_sort(vector, TAM);
  print(vector,TAM);

  return 0;
}
*/
