import java.util.Scanner;
public class Methods
{
	
//create method without returning any value
public static void getRequirements()
{
	//display operational messasges
	System.out.println("Developer: Christopher Valverde");
	System.out.println("Program lists number of characters in a line of text.");
}
public static void lineAnalysis()
{
	Scanner sc = new Scanner(System.in);

		String userLine = "";
		char userChar = ' ';
		int charCount = 0;

		System.out.print("Enter line of text: ");
		while(!sc.hasNextLine())
		{
			System.out.println("Invalid input!\n");
			sc.nextLine();
			System.out.print("Please try again. Enter your first value: ");
		}
		userLine = sc.nextLine ();

		System.out.print ("Enter character to check: ");
		while(!sc.hasNextLine())
		{
			System.out.println("Invalid input!\n");
			sc.nextLine();
			System.out.print("Please try again. Enter your first value: ");
		}
 userChar = sc.next().charAt(0);

 for(int i = 0; i < userLine.length(); i++)
 {
 	if(userLine.charAt(i) == userChar)
 	{
 		charCount++;
 	}
 }
 System.out.println("Number of characters in line of text: " + userLine.length());
 System.out.println("The character " + userChar + " appears " + charCount + " time(s) in the line of text.");
 System.out.println("ASCII value: " + (int) userChar);
 }
}