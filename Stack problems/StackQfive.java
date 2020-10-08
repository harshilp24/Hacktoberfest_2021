import java.util.*;
class StackQfive
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
Stack<Integer> s=new Stack<Integer> ();
Stack<Integer> a=new Stack<Integer> ();

for(int i=0;i<n;i++)
{
int v=sc.nextInt();
s.push(v);
a.push(v);
}


for(int o=0;o<n;o++)
{
System.out.print(s.pop()+" ");
}
System.out.println(" ");
System.out.println(a);
a.pop();
a.pop();
for(int e=0;e<n;e++)
{
System.out.println(a.pop()+" ");
}
}
}