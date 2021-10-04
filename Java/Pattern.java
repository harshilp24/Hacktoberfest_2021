import java.util.Scanner;

public class Pattern
{
    public static void main(String[] args)
    {
      
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of rows : ");

        int rows = scanner.nextInt();

        System.out.println("...The Pattern...");

        for (int i = 1; i <= rows; i++)
        {
            for (int j = rows; j > i; j--)
            {
                System.out.print(" ");
            }
            for (int k = 1; k <= i; k++)
            {
                System.out.print(k);
            }
            for (int l = i - 1; l >= 1; l--)
            {
                System.out.print(l);
            }
            System.out.println();
        }
    }
}