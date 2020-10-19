import java.util.Scanner;

public class ReverseNumber
{
	public static void main(String[] args)
	{
		int n,rev=0; 
		Scanner sc= new Scanner(System.in);
		System.out.println("Enter The Number : ");
		n = sc.nextInt();
		System.out.print("Reverse Of "+n+" is ");
		while(n>0)
		{
			System.out.print((rev*10)+n%10);
			n=n/10;
		}
	}
}