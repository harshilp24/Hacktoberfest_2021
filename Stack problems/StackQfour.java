import java.util.*;
class StackQfour
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
Stack<Integer> s=new Stack<Integer> ();

for(int i=0;i<n;i++)
{
int v=sc.nextInt();
s.push(v);
}
System.out.println("Deleted element is "+s.pop());
System.out.println("The elemenets in STACK");

for(int o=0;o<n;o++)
{
System.out.println(s.pop());
}

}
}