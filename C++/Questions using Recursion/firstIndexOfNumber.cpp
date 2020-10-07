#include<iostream>
using namespace std;

int firstIndex(int input[], int size, int x) {
    if(size==1){
       if(input[0]==x)
           return 0;
       else
           return -1;
    }
    
    if(input[0]==x)
        return 0;
    else{
    int index=firstIndex(input+1,size-1,x);
        if(index != -1) 
            return index+1;
        else
            return -1;
    }

}
int main(){
    int n;
    cin >> n;
  
    int *input = new int[n];
    
    for(int i = 0; i < n; i++) {
        cin >> input[i];
    }
    
    int x;
    
    cin >> x;
    
    cout << firstIndex(input, n, x) << endl;

}


