// bugs added by mckenzie (3 bugs)

public class sum_even_fibonacci {
    public static void main(String[] args) {
     //Initializes variables a and b as integers
        int a = 0, b = 1;
        //Intializes sum_even variable
        int sumEven = 0;
        //while loop loops until b is even 
        while (b < 4000000) {
            if (b % 2 == 0) { // % was replaced with // Fixed
                sumEven += b; // needs to be += // Fixed
            }
            //Set temp variable to b, b is the sum of a and b, and set a to temp
            int temp = b;
            b = a + b;
            a = temp;
        }
        //Print sum even variable
        system.out.println(sumEven) //outfunction needs to be in java // Fixed
    }
}

// answer should be 4613732
