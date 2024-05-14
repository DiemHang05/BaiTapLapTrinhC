#include <stdio.h>
#include <math.h>

int isPerfectSquare(int num) {
    int squareRoot = sqrt(num);
    return (squareRoot * squareRoot == num);
}

int countPerfectSquares(int n) {
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            count++;
        }
    }
    return count;
}

void printPerfectSquares(int n) {
    printf("Cac so chinh phuong nho hon %d la:\n", n);
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    int n;
    printf("Nhap vao mot so nguyen duong: ");
    scanf("%d", &n);

    int count = countPerfectSquares(n);
    printf("Tong so chinh phuong nho hon %d la: %d\n", n, count);

    printPerfectSquares(n);

    return 0;
}