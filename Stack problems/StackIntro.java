import java.util.*;
class StackIntro
{
public static void main(String args[])
{

System.out.println("Staic: Using arrays we can implement stacks, Dynamic: Using linkedlist we can implement stack");
Stack<Integer> s1=new Stack<Integer>();
s1.push(1);
s1.push(2);
s1.push(3);
s1.push(4);
s1.push(5);
s1.push(6);
System.out.println(s1);
System.out.println(s1.pop());
System.out.println(s1.pop());
System.out.println(s1);
System.out.println("  ");


Stack<String> s2=new Stack<String>();
s2.push("Ankita");
s2.push("Ankit");
s2.push("Anki");
s2.push("Ank");
s2.push("An");
s2.push("A");
System.out.println(s2);
System.out.println(s2.pop());
System.out.println(s2.pop());
System.out.println(s2);
System.out.println("  ");

//The java.util.Stack.peek() method in Java is used to retrieve or fetch the first element of the Stack or the element present at the top of the Stack.The element retrieved does not get deleted or removed from the Stack

System.out.println("Trying stack.peek()");
System.out.println(s2.peek());
System.out.println(s2);
System.out.println("  ");

//The java.util.Stack.empty() method in Java is used to check whether a stack is empty or not. The method is of boolean type and returns true if the stack is empty else false

System.out.println("Trying stack.empty()");
System.out.println("Stack before pop is emty or not: "+s2.empty());
System.out.println(s2);
//s2.pop();
//s2.pop();
//s2.pop();
//s2.pop();
//System.out.println("Stack after pop is emty or not: "+s2.empty());
System.out.println("  ");

//The java.util.Stack.search(Object element) method in Java is used to search for an 
//element in the stack and get its distance from the top.
//This method starts the count of the position from 1 and not from 0.
//The method returns its position if the element is successfully found and returns -1
//if the element is absent.
//The element that is on the top of the stack is considered to be at position 1. If more  
//than one element is present, the index of the element closest to the top is returned

System.out.println("Trying stack.search(element)");
System.out.println(s2);
System.out.println("The element position: "+s2.search("Ankita"));
System.out.println("The element position: "+s2.search("kita"));



}
}