import java.util.Scanner;

public class Methods {
    public static void getRequirements(){
        System.out.println("Developer: Efner Pierre");
        System.out.println("Program evaluates largest of three integers.");
        System.out.println("Note: Program checks for integers and non-numeric values.");
      
        System.out.println();
    }
    public static void validateUserInput(){
        Scanner sc = new Scanner(System.in);
        int num1 = 0, num2 = 0, num3 = 0;

        System.out.print("Please enter first number:");
        while(!sc.hasNextInt())
            {
             System.out.println("Not valid integer!\n");
             sc.next();
             System.out.print("Please try again. Enter first number:");
            }
        num1 = sc.nextInt();

        System.out.print("\nPlease enter second number:");
        while(!sc.hasNextInt())
            {
             System.out.println("Not valid integer!");
             sc.next();
             System.out.print("Please try again. Enter second number:");
            }
        num2 = sc.nextInt();

        System.out.print("\nPlease enter third number:");
        while(!sc.hasNextInt())
            {
             System.out.println("Not valid integer!\n");
             sc.next();
             System.out.print("Please try again. Enter third number:");
            }

        num3 = sc.nextInt();

        System.out.println();

        getLargestNumber(num1, num2, num3);
    }

    public static void getLargestNumber(int num1, int num2, int num3)
    {
    System.out.println("Numbers entered: " + num1 + ", " + num2 + ", " + num3);

     if (num1 > num2 && num1 > num3 )
        System.out.println(num1 + " is largest.");
     else if ( num2 > num1 && num2 > num3)
        System.out.println(num2 + " is largest.");
     else if (num3 > num1 && num3 > num2 )
        System.out.println(num3 + " is largest.");
     else
        System.out.println("Integers are equal.");

}
}
