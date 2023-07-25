import java.util.Scanner;

public class Methods 

{
    public static void getRequirements(){

        System.out.println("Program loops through array of strings");
        System.out.println("Use following values: dog, cat, bird, fish, insect");
        System.out.println("Use following loop strctures: for, enhanced for, while, do...while.");
        System.out.println("");
        System.out.println("Note: Preset loops: Pretest loops: for, enhanced for, while. Posttest loop: do...while.");
    }

    public static void arraysandLoops(){

        String[] animals = {"dog", "cat", "bird", "fish", "insect"};


        System.out.println();
        System.out.println("for loop:");
        for(int f = 0; f <animals.length; f++){
            System.out.println(animals[f]);
        }

        System.out.println();
        System.out.println("Enhanced for loop:");
        for (String animal : animals) {
            System.out.println(animal); 
        }
        
        System.out.println();
        System.out.println("while loop:");
        int f = 0;
        while (f < animals.length) {
            System.out.println(animals[f]);
            f++;
          }

        System.out.println();
        System.out.println("do...while loop:");
        int j = 0;
        do{
            System.out.println(animals[j]);
            j++;
        }while(j < animals.length);

        System.out.println();
    }

}
