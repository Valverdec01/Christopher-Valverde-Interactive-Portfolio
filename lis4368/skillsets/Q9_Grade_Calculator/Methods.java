import java.util.Scanner;

public class Methods
{
	
//create method without returning any value
public static void getRequirements()
{
	//display operational messasges
	System.out.println("Developer: Christopher Valverde");
}
public static void getScore(){
        Scanner sc = new Scanner(System.in);
        double score = 0.0;

        System.out.print("Please enter a grade value between 0 and 100: ");
        while (!sc.hasNextDouble()){
            System.out.println("Invalid number!");
            sc.next();
            System.out.print("Please try again. Enter a grade value between 0 and 100:");
        }
        score = sc.nextDouble();
        getGrade(score);

        sc.close();
    }

    public static void getGrade(double score){
        String grade = "";
        if(score < 0 || score > 100){
            System.out.println("Out of range!");
            getScore();
        } 
        else 
        {
            if (score < 60 && score >=0)
                grade = "F";

            else if (score < 63 && score >= 60)
                grade = "D-";

                else if (score < 67 && score >= 63)
                grade = "D";

                else if (score < 70 && score >= 67)
                grade = "D+";

                else if (score < 73 && score >= 70)
                grade = "C-";

                else if (score < 77 && score >= 73)
                grade = "C";

                else if (score < 80 && score >= 77)
                grade = "C+";

                else if (score < 83 && score >= 80)
                grade = "B-";

                else if (score < 87 && score >= 83)
                grade = "B";

                else if (score < 90 && score >= 87)
                grade = "B+";

                else if (score < 93 && score >= 90)
                grade = "A-";

                else
                grade = "A";

            System.out.printf("Score entered: %f%n", score);
            System.out.printf("Final grade: %s%n", grade);

        }   

    }
}