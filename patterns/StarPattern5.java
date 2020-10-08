import java.util.*;
class StarPattern5
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
System.out.println("Enter the number of star rows you want to print: ");
int a=sc.nextInt();
for(int k=1;k<=a;k++)
{
for(int l=a;l>=k;l--)
{
System.out.print(" ");
}
System.out.print("*");
System.out.println();
}

}
}