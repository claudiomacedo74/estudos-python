#include <stdio.h>

int main() {

    float vetor[12];
    float i;
    float soma = 0;

    for(i = 0; i < 12; i++) {
        scanf("%f", &vetor[i]);
        soma += vetor[i];
    }

printf("A SOMA DOS NUMEROS E %.2f", soma);

    return 0;
}



