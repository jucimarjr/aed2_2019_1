#include "io.h"
#include "sort.h"
#define TAM 1000

int main(){
  int vector[TAM];
  read(vector, TAM);
  selection_sort(vector, TAM);
  print(vector, TAM);
}
