#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char* x, char* y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}


void permute(char* a, int l, int r, FILE *ofp, int n)
{
    int i;
    if (l == r){
        for(i = 0; i<n; i++){
            fprintf (ofp, "%c", a[i]);
        }
        fprintf(ofp, "\n");
    }
    else {
        for (i = l; i <= r; i++) {
            swap((a + l), (a + i));
            permute(a, l + 1, r, ofp, n);
            swap((a + l), (a + i)); // backtrack
        }
    }
}

/* Driver program to test above functions */
int main()
{
    FILE *ifp, *ofp;
	ifp = fopen("Entrada2.txt", "r");
    ofp = fopen("Saida2.txt", "w");

    int n;
    fscanf(ifp, "%d", &n);

    char str[100];
    //printf("%c", str[1]);

    for(int i=0;i < n;i++){
        str[i] = i+1+'0';
        //printf("%c", str[i]);
    }


    permute(str, 0, n - 1, ofp, n);

    fclose(ofp);
	fclose(ifp);

    return 0;
}








