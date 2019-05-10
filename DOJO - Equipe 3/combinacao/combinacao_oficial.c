#include<stdio.h>
#include<stdlib.h>

int main(int argc, char const *argv[])
{
  int *vector;
  int i,j,k;
  int x,y;

  printf("X COMB: ");
  scanf("%d",&x);
  printf("Y NUM: ");
  scanf("%d",&y);

  vet = (int*) malloc(y * sizeof(int));

  for(i = 0; i < y; i++)
  {
    printf("vector[%d]: ",i);
    scanf("%d", &vector[i]);
  }

  for(i = 0; i < y; i++)
  {
    for(j = i+1; j < y-(x-2);j++)
    {
      printf("%d", vet[i]);
      for(k = j; k < j+x-1;k++)
      {
        printf(",%d", vet[k]);
      }
      printf("\n");

    }
  }
  return 0;
}
