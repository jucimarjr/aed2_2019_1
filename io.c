#include <stdio.h>
#define TAM 1000

int * create_vector(int vector[])
{
      for (int i = 0; i < size; i++)
      {
        scanf("%i", (vector + i));
      }
      return vector;
}
void print_vector(int vector[])
{
  for (int i = 0; i < size; i++)
  {
    printf("%i ", *(vector + i) );
  }
  printf("\n");
}
