#include <stdio.h>

void inBoiCua7(int dau, int cuoi) {
  for (int i = dau; i <= cuoi; i++) {
    if (i % 7 == 0 && i < 100) {
      printf("%d ", i);
    }
  }
}

int main() {
  printf("Cac so nguyen co 2 chu so va la boi cua 7 la: ");
  inBoiCua7(10, 99);

  return 0;
}