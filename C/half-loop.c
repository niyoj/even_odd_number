#include <stdio.h>
int main()
{
    int num, i, temp;
    printf("Enter any integer:- ");
    scanf("%d", &num);
    temp = num;
    for (i=1; i<=(temp/2); i++)
    {
        num = num-2;
    }
    if (num==0)
    {
        printf("%d is even number. \n", temp);
    }
    else
    {
        printf("%d is odd number. \n", temp);
    }
    return 0;
}