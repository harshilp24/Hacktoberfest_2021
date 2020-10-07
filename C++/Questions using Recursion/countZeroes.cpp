#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    cout << countZeros(n) << endl;
}

int countZeros(int n) {
    // Write your code here
    if(n==0)
        return 1;
    if(n<10)
        return 0;
    else if(n%10==0)
        return 1+countZeros(n/10);
    return countZeros(n/10);
}


