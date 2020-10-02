#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main() {
    int k;
    cin >> k;
    cout << fixed << setprecision(5);
    cout << geometricSum(k) << endl;   
}

double geometricSum(int k) {
    // Write your code here
    if(k==0)
        return 1;
    double ans = 1 / (double)pow(2, k) + geometricSum(k - 1); 
    return ans;
}


