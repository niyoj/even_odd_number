#include <stdio.h>      //Preprocessor directives to include copy of file stdio.h

int main(void) {
    int num;

    printf("\nEnter a number to check: ");
    scanf("%d", &num);

    printf("The number %d is ", num);
    if(num%2 ==0)
        printf("even.");
    else 
        printf("odd.");

    printf("\n\n");
    return 0;       //Keeping the compiler happy
}