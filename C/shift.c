#include <stdio.h>

int main() {
    int num;
    printf("Enter a number for find even or odd: ");
    scanf("%d",&num);
    
    printf("The number %d is ", num);
10
    if(((num>>1)<<1)==num )
        printf("even.");
    else
        printf("odd.");

    printf("\n\n");
    return 0;
}