#include <stdio.h>

int fatorial(int x){
    if (x == 0) {
        return 1;
    }
    else
    {
        return (x * (fatorial (x-1)));
    }
}

int main(int argc, char const *argv[])
{
    int num;
    scanf("%d", &num);
    int resultado = (fatorial(num));
    printf("%d\n", resultado);
    return 0;
}

