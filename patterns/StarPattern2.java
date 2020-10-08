import java.util.*;
class StarPattern2
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
System.out.println("Enter the number of star rows you want to print: ");
int a=sc.nextInt();
for(int i=1;i<=a;i++)
{
for(int j=a;j>=i;j--)
{
System.out.print("*");
}
System.out.println();
}
}
}