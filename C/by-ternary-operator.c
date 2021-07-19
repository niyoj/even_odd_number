#include <stdio.h>
void oddeven (int);
int main()
{
    int num;
    printf("Enter number to check odd or even:- ");
    scanf("%d", &num);
    oddeven (num);
    return 0;
}
void oddeven (int num)
{
    (num%2!=0) ? printf("%d is odd number. \n", num): printf("%d is even number. \n", num);
}