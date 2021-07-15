#include <stdio.h>
#include <math.h>

int main(void) {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    printf("The number %d is ", num);
    
    if(pow(-1, num) == 1)           //when -1 is raised to power of even number result is 1 for odd it is -1
        printf("even.");
    else 
        printf("odd.");

    printf("\n\n");
    return 0;
}