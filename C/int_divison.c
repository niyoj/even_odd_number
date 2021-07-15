#include <stdio.h>      //Preprocessor directives to include copy of file stdio.h

int main(void) {
    int num, temp;

    printf("\nEnter a number to check: ");
    scanf("%d", &num);

    temp = num;
    
    printf("The number %d is ", num);
    if(temp/2*2 == num)
        printf("even.");
    else 
        printf("odd.");

    printf("\n\n");
    return 0;       //Keeping the compiler happy
}