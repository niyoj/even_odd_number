#include <stdio.h>                              //file `stdio.h` contains function `printf()`

//In this program, we check whether a number is even or odd by looping from 1 to n. In each loop a variable (initialy 0) is increased by 1 and if in last loop it was increased in the next loop it is decreased by 1. So, after nth loop if -1 and +1 is repeated for even times it is zero else it is non-zero. Thus, zero means even and non-zero means odd.
int main(void) {
    int num, last_added, a;                     
    last_added = a = 0;                         //var `last_added` stores boolean whehter it was last added (1) in a or not(0)

    printf("Enter a number to be checked: ");   //asks input from the user
    scanf(" %d", &num);                         //takes input from the user and stores in num
    printf("\nThe number %d is ", num);       
    
    for(int i=num; i>=1; i--) {                 //loops from 1 to n
        if(last_added) {                        //if last time was incremented decrease by 1
            last_added = 0;
            a--;
        } else {                                //if last time decremented increase by 1 
            last_added = 1;
            a++;
        }   
    }

    printf((a)? "odd": "even");                 //if final `a` is 0 it is even as 1-1 is 0 else odd
    printf("\n");              
    return 0;                                   //Keeping the compiler happy
}