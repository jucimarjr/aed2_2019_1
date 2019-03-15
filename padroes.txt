TODAS as funçoes de entrada, saida e "sorts" :
- RRECEBE de parâmetro UM (1) vetor de entrada (desordenado)
- RETORNA UM (1) vetor (ordenado)
-------------------------------------------------------------------------
TAMANHO padrão para todos é 1000 
#define TAM 1000
-------------------------------------------------------------------------
ENTRADA e SAIDA em um só arquivo chamado I/O.c
-------------------------------------------------------------------------
TODAS as funçoes e VARIAVEIS em INGLES, nome do VETOR DE ENTRADA será **VECTOR**, logo
TODAS as funções precisarão de uma variável para armazenar o vetor ordenado, que será chamado de **VECTOR_AUX**

Ex:
int xxxxx_sort(int vector)
{
  int vector_aux[TAM];
  //code
  return vector_aux;
}
-------------------------------------------------------------------------
TODOS os arquivos deverão importar o **io.h**, e não o **io.c**
TODOS os arquivos deverão ter no cabeçalho #define TAM 1000
-------------------------------------------------------------------------
Na MAIN, deverá ser criada uma variavel com nome RESULT para armazenar a saída do sort e uma variável com nome VECTOR para armazenar o vetor inicial.
Ex:
int main()
{
  int vector[TAM];
	int result[TAM];
  
  read(vector);
	result = xxx_sort(vector);
	print(result);
  
  return 0;
}
