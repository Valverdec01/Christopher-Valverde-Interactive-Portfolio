import java.util.Scanner;

public class Methods{

    public static void getRequirements(){
        System.out.println("Developer: Christopher Valverde");
        System.out.println("Program evaluates user-entered characters.");
        System.out.println("Use following characters: W or w, C or c, H or h, N or n.");
        System.out.println("Use following decision structures: if...else, and switch.");
        System.out.println();

    }

    public static void decisionStructures(){
        System.out.println("Phone types: W or w (work), C or c (cell), H or h(home), N or n (none)");
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter phone type: ");
        char pType = in.next().charAt(0);

        System.out.println();
        System.out.println("if...else:");
        
        if(pType == 'W' | pType == 'w'){
            System.out.println("Phone type: Work");
        }
        else if(pType == 'C' | pType == 'c'){
            System.out.println("Phone type: Cell");
        }
        else if(pType == 'H' | pType == 'h'){
            System.out.println("Phone type: Home");
        }
        else if(pType == 'N' | pType == 'n'){
            System.out.println("Phone type: None");
        }
        else{
            System.out.println("Incorrect character entry");
        }

        System.out.println();
        System.out.println("switch: ");

        switch (pType){
            case 'W':
                System.out.print("Phone Type: Work");
                break;
            case 'w':  
                System.out.print("Phone Type: Work");
                break;
            case 'C':
                System.out.print("Phone Type: Cell");
                break;
            case 'c':
                System.out.print("Phone Type: Cell");
                break;
            case 'H': 
                System.out.print("Phone Type: Home");
                break;
            case 'h': 
                System.out.print("Phone Type: Home");
                break;
            case 'N': 
                System.out.print("Phone Type: None");
                break;
            case 'n': 
                System.out.print("Phone Type: None");
                break;
            default: 
                System.out.print("Incorrect character entry");
                     break;
        }
        in.close();
    }
}
