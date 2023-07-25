import java.util.*;
public class Methods
{
    //Create Method without returning any value (without object)
    public static void getRequirements()
    {
        // display operational messages
        System.out.println("Developer: Christopher Valverde");   
        System.out.println("Program Requirements: ");
        System.out.println("1. Program swaps two user-entered floating-point values.");
        System.out.println("2. Create at least two user-defined methods: getRequirement() and numberSwap().");
        System.out.println("3. Must perform data validation: number must be floats.");
        System.out.println("4. Print numbers before/after swapping.");
        System.out.println(); // print a blank line 
    }

    public static void numberSwap()
    {
        float num1, num2, num3;

        System.out.print("Enter num1: ");
        Scanner scan = new Scanner(System.in);
        while (true)
        {
            try
            {
                num1 = scan.nextFloat();
                break;
            }
            catch (InputMismatchException e)
            {
                System.out.println("invalid input!");
                System.out.println(); //blank line
                System.out.print("Please try again. Enter num1: ");
                scan.nextLine();
                System.out.println(); //blank line
            }
        }

        System.out.print("Enter num2: ");
        while (true)
        {
            try
            {
                num2 = scan.nextFloat();
                break;
            }
            catch (InputMismatchException e)
            {
                System.out.println("invalid input!");
                System.out.println(); //blank line
                System.out.print("Please try again. Enter num2: ");
                scan.nextLine();
                System.out.println(); //blank line
            }
        }

        System.out.println(); //blank line
        System.out.println("Before swap:");
        System.out.println("num1 = " + num1);
        System.out.println("num2 = " + num2);
        System.out.println(); //blank line

        num3 = num1;
        num1 = num2;
        num2 = num3;

        System.out.println("After swap:");
        System.out.println("num1 = " + num1);
        System.out.println("num2 = " + num2);

    }
}