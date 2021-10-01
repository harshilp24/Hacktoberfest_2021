#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution
{
public:
    vector<int> singleNumber(vector<int> nums) 
    {
        // Code here.
        vector<int> v;
        int num1=0;
        for(auto it: nums) {
            num1^=it;
        }
        int temp = num1,c=0;
        while(temp) {
            if(temp&1) {
                break;
            }
            c++; temp=temp>>1;
        }
        int mask = 1<<c,num2=0;
        for(auto it: nums) {
            if((mask&it)>>c) {
                num2^=it;
            }
        }
        num1^=num2;
        v.push_back(min(num1,num2));
        v.push_back(max(num1,num2));
        return v;
    }
};

// { Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
    	int n; 
    	cin >> n;
    	vector<int> v(2 * n + 2);
    	for(int i = 0; i < 2 * n + 2; i++)
    		cin >> v[i];
    	Solution ob;
    	vector<int > ans = ob.singleNumber(v);
    	for(auto i: ans)
    		cout << i << " ";
    	cout << "\n";
    }
	return 0;
}  
