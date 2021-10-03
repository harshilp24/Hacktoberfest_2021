#include <iostream>

using namespace std;

void krishnamurty(int n) 
{
    int b=0,sum=0,m=n;
    while(n>0) //cutting the digits
    {
        b=n%10;  
        int f=1;
        for(int i=1;i<=b;i++) //factorial
        {
           f=f*i; 
        }
    sum=sum+f; //sum of each factorials
    n=n/10;
    }
    
    if(m==sum)
    cout<<m<<" is a krishnamurty no.\n";
    else
    cout<<m<<" is not a krishnamurty no.\n";
}

int main()
{
   int n;
   cout<<"Enter a number:\n";
   cin>>n;
   krishnamurty(n);
    return 0;
}
