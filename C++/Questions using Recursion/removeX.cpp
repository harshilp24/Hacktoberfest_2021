#include <iostream>
using namespace std;

void removeX(char input[]) {
    // Write your code here
    if(input[0]=='\0')
        return;
    if(input[0]=='x'){
        int i=1;
        for(;input[i]!='\0';i++)
            input[i-1]=input[i];
        input[i-1]=input[i];
        removeX(input);
    }
    removeX(input+1);
}
int main() {
    char input[100];
    cin.getline(input, 100);
    removeX(input);
    cout << input << endl;
}

