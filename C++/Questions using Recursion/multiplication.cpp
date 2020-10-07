#include <iostream>
using namespace std;

int multiplyNumbers(int m, int n) {
    // Write your code here
    if(m==0)
    {
        return 0;
    }
    int result=(m*n);
    return result;
}
int main() {
    int m, n;
    cin >> m >> n;
    cout << multiplyNumbers(m, n) << endl;
}
