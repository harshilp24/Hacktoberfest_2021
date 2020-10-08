import java.util.*;
class StackQone
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
Stack<String> s=new Stack<String> ();
String value=sc.nextLine();
String[] m=value.split("");

for(int i=0;i<m.length;i++)
{
String v=m[i];
s.push(v);
}
for(int o=0;o<m.length;o++)
{
System.out.print(s.pop());
}
}
}