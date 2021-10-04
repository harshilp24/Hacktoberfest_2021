import java.util.Scanner;

public class Fibonacci {

    public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the range : ");
		int n = sc.nextInt();
		System.out.println("Enter the First term : ");
		int f = sc.nextInt();
		System.out.println("Enter the Second term : ");
		int s = sc.nextInt();
        System.out.println("First " + n + " terms Are ");

        for (int i = 1; i <= n; ++i)
        {
            System.out.print(f + " , ");

            int sum = f + s;
            f = s;
            s = sum;
        }
    }
}