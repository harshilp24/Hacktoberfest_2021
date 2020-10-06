#include <math.h>
#include <stdio.h>

int main() 
{
   int num, org_num, rem, n = 0;
   float res = 0.0;

   printf("Enter an integer: ");
   scanf("%d", &num);
   org_num = num;
  
   for (org_num = num; org_num != 0; ++n) 
       org_num /= 10;
  
   for (org_num = num; org_num != 0; org_num/= 10) 
   {
       rem = org_num % 10;
       res += pow(rem, n);
   }

   if ((int)res == num)
    printf("%d is an Armstrong number!", num);
   else
    printf("%d is not an Armstrong number!", num);
   return 0;
}
