#include <stdio.h>
int main()
{
    int num;
    printf("Enter number to check odd or even:- ");
    scanf("%d", &num);
    (num%2!=0) ? printf("%d is odd number. \n", num): printf("%d is even number. \n", num);
    return 0;
}
