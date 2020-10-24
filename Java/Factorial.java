import java.util.*;
public class Factorial {
            public static void main(String [] args){
                    int fact = 1;
                    System.out.println("Enter a number");
                    Scanner sc = new Scanner(System.in);
                    int num = sc.nextInt();
                    int i = num;
                    while(i>0){
                            fact = fact * i;
                            i--;
                    }
                    System.out.println("Factorial is: "+  fact);
                }
}
