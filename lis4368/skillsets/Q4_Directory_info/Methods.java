import java.io.File;
import java.util.Scanner;

public class Methods
{
	
//create method without returning any value
public static void getRequirements()
{
	//display operational messasges
	System.out.println("Developer: Christopher Valverde");
	System.out.println("Program lists files and subdirectories of *user*-specfied directory.\n");
}

public static void directoryInfo()
{
String userDir = "";
Scanner sc = new Scanner(System.in);

System.out.print ("Please enter directory path: ");
userDir = sc.nextLine();

File directoryPath = new File(userDir);
File fileList[] = directoryPath.listFiles();

System.out.println("List files and directories in specified directory:");
for(File file : fileList)
{
System.out.println("Name: " + file.getName());
System.out.println("Path: " + file.getAbsolutePath());
System.out.println("Size (Bytes): " + file.length());
System.out.println("Size (KB): " + file.length()/(1024));
System.out.println("Size (MB): " + file.length()/(1024*1024));
System.out.println();
}

sc.close();
 }
}