// Kadane's algorithm is used to find maximum subarray sum
//code contributed by devanshi katyal
#include <iostream>
using namespace std;
int kadane(int *a, int n){
    int glosum=a[0], currsum=a[0];
    for(int i=1;i<n;i++){
        currsum= max(a[i], currsum+a[i]);
        if(currsum>glosum){
            glosum= currsum;
        }
    }
    return glosum;
}


int main() {
	    int n;
	    cin>>n;
	    int a[n];
	    for(int j=0;j<n;j++){
	        cin>>a[j];
	    }
	    int ans= kadane(a,n);
	    cout<<ans;

	return 0;
}
