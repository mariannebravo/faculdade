#include <stdio.h>

int main(void) {
  float alt1;
  float alt2;
  float alt3;

  printf("Informe altura da primeira pessoa: ");
  scanf("%f", &alt1);

  printf("Informe altura da segunda pessoa: ");
  scanf("%f", &alt2);

  printf("Informe altura da terceira pessoa: ");
  scanf("%f", &alt3);

  if (alt1 == alt2 && alt1 == alt3) {
    printf("As alturas são iguais");
  } 
    else if (alt1 > alt2 && alt1 > alt3) {
      printf("A altura da primeira pessoa é a maior. Altura inserida: %f", alt1);
  } 
    else if (alt2 > alt1 && alt2 > alt3) {
      printf("A altura da segunda pessoa é a maior. Altura inserida: %f", alt2);
  } 
    else if (alt3 > alt1 && alt3 > alt2) {
      printf("A altura da terceira pessoa é a maior. Altura inserida: %f", alt3);
  }

}
