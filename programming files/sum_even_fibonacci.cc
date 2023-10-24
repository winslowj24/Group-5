#include <iostream>

int main()
{
    //Initializes variables a and b as integers
    int a = 0, b = 1;
    //sum_even variable is declared as integer 0
    int sum_even = 0;
    //While loop 
    while (b < 4000000) {
        //if b is even then add it to sum_even else set temp to b and set b to be the sum of a and b, set a to temp.
        if (b % 2 == 0) {
            sum_even += b;
        }
        int temp = b;
        b = a + b;
        a = temp;
    }
    //Print sum_even variable
    std::cout << sum_even << std::endl;

    return 0;
}

// answer should be 4613732
