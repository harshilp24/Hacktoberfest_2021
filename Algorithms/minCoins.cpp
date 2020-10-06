//Find minimum number of coins that make a given value

#include <iostream>
#include <cstring>
#include <vector>
#include <climits>

using namespace std;

int dp[1005];

int minCoins(vector<int> & v, int x){
    if(x == 0) return 0;
    if(dp[x] != -1) return dp[x];
    int res = INT_MAX;

    for(int i = 0; i < v.size(); i++){
        if(v[i] <= x){
            int sub_res = minCoins(v, x- v[i]);
            if(sub_res != INT_MAX && sub_res + 1 < res){
                res = sub_res + 1;
            }
        }
    }
    return dp[x] = res;
}


int main(){
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(0);
    
    vector<int> a;
    int N, M, aux;
    cin >> N >> M;
    for(int i = 0; i < N; i++){
        cin >> aux;
        a.push_back(aux);
    }
    memset(dp, -1, sizeof(dp));
    int quantity = minCoins(a, M);
    cout << quantity << endl;
    
    
    return 0;
}