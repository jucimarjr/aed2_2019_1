#include "io.h"
#include "bubble_sort.c"
#include "selection_sort.c"
#define TAM 1000

int main(){
  int vector[TAM];
  create_vector(vector, TAM);
  selection_sort(vector, TAM);
  print_vector(vector, TAM);
}
