#include<iostream>
using namespace std;
int main()
{
    string s;
    cout<<"enter a digit";
    cin>>s;
    int n=s.find(".");
    if(n==string::npos)
     cout<<"";
    else
        cout<<s.substr(n+1);
    return 0;

}
