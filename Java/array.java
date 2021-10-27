//Java Program to illustrate how to declare, instantiate, initialize  
//and traverse the Java array. 
import java.util.Scanner;
class Testarray{  
public static void main(String args[]){  
  //Take input from user in array and calculate average
  Scanner sc = new Scanner(System.in);
  int[] arr = new int[10];
  int sum=0;
  System.out.println("Enter 10 values in array: ");
  for(int i=0;i<10;i++){
    arr[i] = sc.nextInt();
    sum+=arr[i];
  }
  System.out.println(Average is: "+sum/10);
  
  
  
int a[]=new int[5];//declaration and instantiation  
a[0]=10;//initialization  
a[1]=20;  
a[2]=70;  
a[3]=40;  
a[4]=50;  
//traversing array  
for(int i=0;i<a.length;i++)//length is the property of array  
System.out.println(a[i]);  
}} 
