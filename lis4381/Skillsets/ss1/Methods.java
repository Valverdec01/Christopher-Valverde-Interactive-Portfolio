import java.util.Scanner;

public class Methods{

    public static void getRequirements(){
        System.out.println("Developer: Christopher Valverde");
        System.out.println("Program evaluates integers as even or odd.");
        System.out.println("Note: Program does *not* check for non-numeric characters");
        System.out.println();
    }

    public static void evaluateNumber(){

        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter a number...");
        int num = in.nextInt();

        if (num % 2 == 0){
            System.out.print(num + " is even");
        }
        else{
            System.out.print(num + " is odd");
        }
        in.close();
    }
}
