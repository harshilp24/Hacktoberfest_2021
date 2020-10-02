#include <iostream>
#include <cstring>
using namespace std;

bool isPalRec(char input[],int s,int e)
{
    if(s==e)
        return true;
    if(input[s]!=input[e])
        return false;
    if(s<e+1)
    return isPalRec(input,s+1,e-1);
    return true;
}
bool checkPalindrome(char input[]) {   
    int n=strlen(input);
    if(n==0)
        return true;
    return isPalRec(input,0,n-1);    
}
int main() {
    char input[50];
    cin >> input;
    
    if(checkPalindrome(input)) {
        cout << "true" << endl;
    }
    else {
        cout << "false" << endl;
    }
}


