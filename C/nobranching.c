#include <stdio.h>
#include <stdbool.h>

bool isOdd_nobranch(int num);

int main(){
    int num = 5;
    bool x = isOdd_nobranch(num);

    return 0;
}

//returns 1 if num is odd, 0 if num is even
// no branching is used, prints directly "Odd or Even"
bool isOdd_nobranch(int num){
    (num & 1 && printf("Odd")) || printf("Even");
    return num & 1;
}