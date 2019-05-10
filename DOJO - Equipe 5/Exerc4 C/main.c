#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printPatternUtil(char str[], char buff[], int i, int j, int n, FILE *ofp)
{
    if (i==n)
    {
        buff[j] = '\0';
        //printf("%s\n", buff);
        fprintf(ofp, "%s\n", buff);
        return;
    }

    // Colocar um caracter
    buff[j] = str[i];
    printPatternUtil(str, buff, i+1, j+1, n, ofp);

    // Colocar um espaco e um caracter
    buff[j] = ' ';
    buff[j+1] = str[i];

    printPatternUtil(str, buff, i+1, j+2, n, ofp);
}

// Essa eh a funcao principal, cria outros para criaar as particoes
void printPattern(char *str, int n, FILE *ofp)
{

    char buf[2*n];

    // O primeiro caracter sempre estara na primeira posicao
    buf[0] = str[0];

    printPatternUtil(str, buf, 1, 1, n, ofp);
}

int main()
{

    FILE *ifp, *ofp;
	ifp = fopen("Entrada4.txt", "r");
    ofp = fopen("Saida4.txt", "w");

    int n;
    fscanf(ifp, "%d", &n);

    //char str[] = "1234";

    char str[100];

    for(int i=0;i < n;i++){
        str[i] = i+1+'0';
    }

    printPattern(str, n, ofp);


    fclose(ofp);
	fclose(ifp);

    return 0;
}
