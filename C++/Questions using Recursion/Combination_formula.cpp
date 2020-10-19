#include <iostream>
using namespace std;

int C(int n,int r)
{
    if(r==0 || n==r)
     return 1;
    else
     return C(n-1,r-1) + C(n-1,r);
}
int main() {
	int n;
	int r;
	cout<<"Combination Formula :\n nCr = n!/(r!*(n-r)!)\n";
	cout<<"Enter the value of n : ";
	cin>>n;
	cout<<"enter the value of r : ";
	cin>>r;
	cout<<"\n"<<n<<"C"<<r<<" : "<<C(n,r);
	return 0;
}
