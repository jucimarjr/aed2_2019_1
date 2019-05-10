
#include <stdio.h>
#include <stdlib.h>

int main()
{
   int *vector;
   int a;
   int b;
   int i;
   int j;
   int c;
   
   printf("Type the total value of the numbers: ");
   scanf("%d", &b);
   vector = (int *) malloc (b*sizeof(int));
   for(i = 0; i < b; i++)
   {
       printf("fill the %d position of the vector: ", i);
       scanf("%d", &vector[i]);
   }
   
   printf("set a value for a: ");
   scanf("%d", &a);
   
   
   for(i = 0; i < b; i++)
   {
       for(j = i+1; j < b-(a-2); j++)
	   {
           printf("%d", vector[i]);
           for(c = j; c < j+a-1; c++)
		   {
               printf(",%d", vector[c]);
           }
           printf("\n");
       }
   }
   
    return 0;
}
