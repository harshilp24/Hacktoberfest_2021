#include<bits/stdc++.h>
using namespace std;
string findAnagram(string s1,string s2)
{
    int n=0;

    if(s1.size()!=s2.size())
         return "no";
         n=s1.size();
    sort(s2.begin(),s2.end());
     sort(s1.begin(),s1.end());
    for(int i=0;i<n;i++)
    {
        if(s1[i]!=s2[i])
            return "no";
    }
    return "yes";
}

int main()
{
  string s1,s2;
  cin>>s1>>s2;
    cout<<findAnagram(s1,s2;
    return 0;
}
