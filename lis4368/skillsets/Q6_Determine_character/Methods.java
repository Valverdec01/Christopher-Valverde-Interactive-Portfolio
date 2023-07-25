import java.util.Scanner;

public class Methods
{
	
//create method without returning any value
public static void getRequirements()
{
	//display operational messasges
	System.out.println("Developer: Christopher Valverde");
	System.out.println("Program determines whether user-entered value is vowel, consonant, special character, or integer. Program displays character's ASCII value.");

}
public static void determineChar()
{
	char ch = ' ';
	char chTest = ' ';
		Scanner sc = new Scanner(System.in);
	System.out.print("Please enter character: ");

	ch = sc.next().charAt(0);
	chTest = Character.toLowerCase(ch);

	if((chTest == 'a' || chTest == 'e' || chTest == 'i' || chTest == 'o' || chTest == 'u' || chTest == 'y'))
	{
		System.out.println(ch + " is a vowel. ASCII value: " + (int) ch);
	}
	else if(ch >= '0' && ch <='9')
	{
		System.out.println(ch + " is an int. ASCII value: " + (int) ch);
	}
	else if((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z'))
	{
		System.out.println(ch + " is a consonant. ASCII value: " + (int) ch);
	}
	else
	{
		System.out.println(ch + " is a special character. ASCII value: " + (int) ch);
	}
	sc.close();

}
}