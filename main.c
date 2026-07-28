#include <stdio.h>

int main() {

    int vetor[20];
    int i;
    int soma = 0;
    int par;
    int impar;

    for(i = 0; i < 20; i++) {
        scanf("%d", &vetor[i]);
    }

    for(i = 0; i < 20; i++) {
        if(vetor[i] % 2 == 0) {
            par++;
        } else {
            impar++;
        }
    }
    printf("NUMEROS PARES: %d\n", par);
    printf("NUMEROS IMPARES: %d\n", impar);
    return 0;
}



