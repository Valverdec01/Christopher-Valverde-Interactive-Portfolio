import java.util.Scanner;

import java.util.Random;
import java.util.Scanner;

public class Methods {

    public static void getRequirements(){
        System.out.println("Developer: Christopher Valverde");
        System.out.println("Print minimum and maximum integers values.");
        System.out.println("Program prompts user to enter desired number of pseudorandom-generated integers (min 1).");
        System.out.println("Use following loop structures: for, enhanced for, while, do...while.");
        System.out.println();

        System.out.println("Integer.MIN_VALUE = " + Integer.MIN_VALUE);
        System.out.println("Integer.MAX_VALUE = " + Integer.MAX_VALUE);

    }
    public static int[] createArray(){
        Scanner in = new Scanner(System.in);
        int arraySize = 0;

        System.out.print("Enter desired number of pseudorandom integers (min 1): ");
        arraySize = in.nextInt();

        int yourArray[] = new int[arraySize];
        return yourArray;
    }
    public static void randomNumberGenerator(int [] myArray){
        Random r = new Random();
        int i = 0;

        System.out.println("for loop:");
        for(i = 0; i < myArray.length; i++){
            System.out.println(r.nextInt());
        }
        System.out.println();

        System.out.println("Enhanced for loop:");
        for(int n: myArray){
            System.out.println(r.nextInt());
        }
        System.out.println();

        System.out.println("while loop:");
        i = 0;
        while(i < myArray.length){
            System.out.println(r.nextInt());
            i++;
        }
        System.out.println();
        
        i = 0;
        System.out.println("do...while loop:");
        do{
            System.out.println(r.nextInt());
            i++;
        }while(i < myArray.length);
    }                                                                                                                                                 
}
