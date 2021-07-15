# Even Odd 
Even odd is a project where we intend to find maximum possible way to check wether a number is even or odd. The main objectives of the program is;
* To demonstrate that there is not just a highway in programming, there are many ways and it depends on your problem solving abillity,
* To share each other approach to a simple solution,
* To know to what extent can we do for this task..

## How to contribute?
1. Fork the project, 
2. Read the README.md file which consists what approach we have taken so far. Such that, your solution would be unique.
3. You can code in any language, but be sure to keep your code in the respective directory for your programming language. If you don't find yours, you can create one.
3. Code, and create a pull request.
4. And yeah, don't forget to write what you have done in `Our approaches` section in README.md file

## Our contributors
* Niyoj Oli @niyoj
* You too can be here

## Our approaches
* We used simple modulus operator to check wether a number is perfectly divisible by 2 or not in `modulus.c`.
* We used bitwise and operator **&** as even number always ends with 0 and odd with 1 and using **&** operator if it is odd output is non-zero (true) else output is zero (false) in `bitwise_and.c`. 
* We used looping from 1 to n times and in each loop either we add any variable by 1 or subtract it by 1. First it is added, and in second it is decremented and this loop continues. Hence, +1 and -1 is repeated even times for even number so, for even output is 0 (true) and for odd it is non-zero (false) in `loop_1.c`.
* We used concept of integer division i.e. when two integers are divided the value is also converted to intger type. So, even number divided by 2 followed by multiplication 2 is same as the inital number, but in case of odd number diviided by 2 the value consists of decimal part which is removed during integer conversion, so when it is multiplied by 2, it is not same as initial number in `int_divison.c`

