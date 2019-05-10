#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void Combination(int a[], int reqLen, int start, int currLen, bool check[], int len, FILE *ofp)
{
	if(currLen > reqLen)
        return;

	else if (currLen == reqLen)
	{
		for (int i = 0; i < len; i++)
		{
			if (check[i] == true)
			{
			    fprintf (ofp, "%d", a[i]);
				//printf("%d", a[i]);
			}
		}
		fprintf(ofp, "\n");
		return;
	}
	// Se isso for igual não existe elemento restante
	if (start == len)
	{
		return;
	}

	check[start] = true;
	Combination(a, reqLen, start + 1, currLen + 1, check, len, ofp);

	check[start] = false;
	Combination(a, reqLen, start + 1, currLen, check, len, ofp);
}

int main()
{
    FILE *ifp, *ofp;
	int i, n, k;
	ifp = fopen("Entrada1.txt", "r");
    ofp = fopen("Saida1.txt", "w");

    fscanf(ifp, "%d", &n);
    fscanf(ifp, "%d", &k);

	bool check[n];
	int arr[n];


	for(i = 0; i < n; i++)
	{
		arr[i] = i + 1;
		check[i] = false;
	}


	Combination(arr, k, 0, 0, check, n, ofp);

    fclose(ofp);
	fclose(ifp);

	return 0;
}
