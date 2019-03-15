#include <stdio.h>
#define TAM 1000

int read()
{     
      int vector_aux[TAM];
      for (int i = 0; i < TAM; i++)
      {
        scanf("%i", (vector_aux + i));
      }
      return vector_aux; 
}

void print(int vector[])
{
  for (int i = 0; i < TAM; i++)
  {
    printf("%i ", *(vector + i) );
  }
  printf("\n");
}
