#include <iostream>
using namespace std;
int main() {
    int a,n; cin>>a>>n;
    int ans=1;
    while(n) {
        if(n&1) {
            ans=ans*a;
            cout<<ans<<endl;
        }
        n=n>>1;
        a=a*a;
    }
    cout<<ans<<endl;
    return 0;
}
