import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Methods.getRequirements();

        int[] userArray = Methods.createArray();

        Methods.randomNumberGenerator(userArray);
    }
}

