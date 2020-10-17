#include <iostream>
using namespace std;
class First
{
public:
void display_1( int a, int b)
{
cout<< "Values of a and b are: "<<a <<" and "<<b<<endl;
}
};
class Second
{
public:
void display_2()
{
cout<< "This is just an empty method for displaying"<<endl;
}
};
class Third: public First,public Second
{
public:
void display_3(float f1, float f2)
{
cout<< "Values of a and b are: "<<f1 <<" and "<<f2<<endl;
}
};
int main()
{
int a;
int b;
cout<<" Enter value for a: "<<endl;
cin>>a;
cout<<" Enter value for b: "<<endl;
cin>>b;
float f1;
float f2;
cout<<" Enter value for float f1: "<<endl;
cin >>f1;
cout<<" Enter value for float f2: "<<endl;
cin>>f2;
Third t;
t.display_1(a,b);
t.display_2();
t.display_3(f1,f2);
}
