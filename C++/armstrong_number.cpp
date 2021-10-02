//Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int n=0;
    cin>>n;
    int sum=0;
    int original=n;
    while(n>0){
        int lastdigit=n%10;
        sum += round(pow(lastdigit,3));
        n = n/10;
    }

    if(sum==original){
        cout<<"Armstrong Number\n";
    }
    else{
        cout<<"Not armstrong\n";
    }
}
