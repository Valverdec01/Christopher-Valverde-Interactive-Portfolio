import java.util.Scanner;

public class Methods
{
	
//create method without returning any value
public static void getRequirements()
{
	//display operational messasges
	System.out.println("Developer: Christopher Valverde");
	System.out.println("\n1. Counts number and types of chaaracters from user-entered string. \n2. Count: total, letters (upper-/lowercase), numbers, spaces and other characters");

}
public static void countChar()
{
	int letter = 0;
	int space = 0;
	int num = 0;
	int upper = 0;
	int lower = 0;
	int other = 0;
	String str = "";

	System.out.print("Please enter string: ");
	 Scanner sc = new Scanner(System.in);
	 str = sc.nextLine();

	 char [] ch = str.toCharArray();

	 for(int i = 0; i < str.length(); i++)
	 {
	 	if(Character.isLetter(ch[i]))
	 	{
	 		if(Character.isUpperCase(ch[i]))
	 		{
	 			upper++;
	 		}
	 		if(Character.isLowerCase(ch[i]))
	 		{
	 			lower++;
	 		}
	 		letter++;
	 		}
	 		else if(Character.isDigit(ch[i]))
	 		{
	 			num++;
	 		}
	 		else if(Character.isSpaceChar(ch[i]))
	 		{
	 			space++;
	 		}
	 		else
	 		{
	 			other++;
	 		}
	 	}

	 	System.out.println("\nYour string: \"" + str + "\" has the following number and types of characters:");
	 	

	 	System.out.println("Total number of characters: " + str.length());
	 	System.out.println("Letter(s): " + letter);
	 	System.out.println("Upper-case letter(s): " + upper);
	 	System.out.println("Lower-case letter(s): " + lower);
	 	System.out.println("number(s): " + num);
	 	System.out.println("Space(s): " + space);
	 	System.out.println("Other character(s): " + other);	
	 	
	 	sc.close();
	 }

}
