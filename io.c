#include <stdio.h>
#define TAM 1000

void read(int * vector)
{
      for (int i = 0; i < TAM; i++)
      {
        scanf("%i", (vector + i));
      }
}

void print(int vector[])
{
  for (int i = 0; i < TAM; i++)
  {
    printf("%i ", *(vector + i) );
  }
  printf("\n");
}
