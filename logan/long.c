#include <stdio.h>

int main() {
    int i;
    unsigned long long int acc = 1L;
    for (i = 0 ; i < 32 ; i++) {
        printf("%d: %qu\n", i, acc);
        acc *= 2;
    }

    printf("%qu\n", acc);

    return 0;
}
