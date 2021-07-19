//This code was added by @khemraj-bit
#include <stdio.h>

int main(void) {
    int num;

    printf("Enter number to check odd or even: ");
    scanf("%d", &num);

    printf("The number %d is an ", num);
    printf((num%2!=0) ? "odd number.": "even number.");
    printf("\n");
    
    return 0;
}
