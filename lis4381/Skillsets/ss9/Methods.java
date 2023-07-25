import java.util.Scanner;
class Methods 
{
    static final Scanner sc = new Scanner(System.in);

    public static void getRequirements()
    {
        System.out.println("Developer: Christopher Valverde");
        System.out.println("1) Program creates arrays size at run-time.");
        System.out.println("2)Program displays array size");
        System.out.println("3)Program rounds sum and average of numbers to two decimal places.");
        System.out.println("4)Numbers *must* be float data type, not double.");

        System.out.println();
    }

    public static int validateArraySize()

    {
        int arraySize=0;

        System.out.print("Please enter array size: ");
        while(!sc.hasNextInt())
        {
            System.out.println("Not valid integer!\n");
            sc.next();
            System.out.print("Please try again. Enter array size: ");
        }
       arraySize= sc.nextInt();
       System.out.println();

       return arraySize;
    }
    
    public static void calculateNumbers(int arraySize)
    {
        float sum = 0.0f;
        float average = 0.0F;

        System.out.print("Please enter " + arraySize +  "numbers.\n");

        float numsArray[] = new float[arraySize];

        for (int i=0; i< arraySize; i++)
        {
            System.out.println("Enter num " + (i+1) + ": " );

            while(!sc.hasNextFloat())
            {
                System.out.println("Not valid number!\n");
                sc.next();
                System.out.print("Please try again. Enter num" + (i+1) + ":");
            }
            numsArray[i]= sc.nextFloat();
            sum = sum + numsArray[i];
        }

        average = sum/arraySize;

        System.out.print("/Numbers entered: ");
        for (int i =0;i < numsArray.length;i++)
        {
            System.out.print(numsArray[i]+ " ");
        }
        printNumbers(sum,average);
   
    }

    public static void printNumbers(float sum, float average)
    {
        System.out.print("\nSum: " + String.format("%.2f", sum));
        System.out.println("Average: " + String.format("%.2f", average));
    }

}   