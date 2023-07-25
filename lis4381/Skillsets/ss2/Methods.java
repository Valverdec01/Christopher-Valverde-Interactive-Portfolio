import java.util.Scanner;

public class Methods {
       
    public static void getRequirements(){
        System.out.println("Program evaluates largest of two integers");
        System.out.println("Note: Program does *not* check for non-numeric characters or non-integer values.");
    }
        
    public static void largestNumber(){
    
    Scanner read = new Scanner(System.in);
    
        System.out.print("Enter first integer: ");
        int num1 = read.nextInt();

        System.out.print("Enter second number: ");
        int num2 = read.nextInt();

        if (num1 > num2){
            System.out.print(num1 + " is larger than " + num2);
        }
        else if(num2 > num1){
            System.out.print(num2 + " is larger than " + num1);
        }
        else{
            System.out.print("Integers are equal");
        }
    }

}


