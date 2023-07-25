
public class Methods
{

    static float[] numArray = new float[]{1.0f,2.1f,3.2f,4.3f,5.4f};
    

    //Create Method without returning any value (without object)
    public static void getRequirements()
    {
        // display operational messages
        System.out.println("Developer: Christopher Valverde");   
        System.out.println("Program loops through array of floats");
        System.out.println("Use following values: 1.0, 2.1, 3.2, 4.3, 5.4");
        System.out.println("Use following loop structures: for, enhanced for, while, do...while.");
        System.out.println(); // print a blank line
        System.out.println("Note: Pretest loops: for, enhanced for, while. Posttest lops: do...while.");
        System.out.println(); // print a blank line 


    }

    public static void forLoop()
    {
        System.out.println("for loop:");
        for (int x = 0; x < numArray.length; x++)
        {
            System.out.println(numArray[x]);
        }
        System.out.println(); // print a blank line 
    }

    public static void enhancedForLoop()
    {
        System.out.println("Enhanced for loop:");
         for (float x : numArray)
         {
            System.out.println(x);
         }
         System.out.println(); // print a blank line 
    }

    public static void whileLoop()
    {
        System.out.println("while loop:");
        int x = 0;
        while (x < numArray.length)
        {
            System.out.println(numArray[x]);
            x++;
        }
        System.out.println(); // print a blank line 
    }

    public static void doWhileLoop()
    {
        System.out.println("do...while loop:");
        int x = 0;
        do
        {
            System.out.println(numArray[x]);
            x++;
        }
        while (x < numArray.length);
        
    }

}