#include <iostream>
#include<cmath>
#include<cstring>
using namespace std;

int stringToNumber(char input[]) {
    // Write your code her
    if (input[0]=='\0')
        return 0;
    int ans=stringToNumber(input+1);
    
    int size=strlen(input);
    int d=(input[0]-48)*pow(10,size-1);
    return ans+d;

}

int main() {
    char input[50];
    cin >> input;
    cout << stringToNumber(input) << endl;
}
