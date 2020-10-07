/*Idea is to take maximum of following two
1.maximum sum of normal subarray.
2.maximum sum of circular sub array(minimum subarray sum -total subarray sum)
*/
#include<bits/stdc++.h>
using namespace std;
int normalMaxSum(int arr[],int n)
{
    int res=arr[0],maxEnding=arr[0];
    for(int i=1;i<n;i++)
    {
      maxEnding = max(arr[i],maxending+arr[i]);
      res=max(res,maxEnding);
     }
     return res;
   }
int OveralMaxSum(int arr[],int n)
{
  int max_normal = normalMaxSum(arr,n);
  if(max_normal>0)
    return max_normal;
  int arr_sum=0;
  for(int i=0;i<n;i++)
  {
      arr_sum+=arr[i];
      arr[i]=-arr[i];
  }
  int max_circular = arr_sum+normalMaxSum(arr,n);
}
//driver code
int main()
{
    int T;
    cin>>T;//tescases
    while(T--)
    {
      int num;
      cin>>num;
      int arr[num];
      for(int i=o;i<num;i++)
        cin>>arr[i];
      cout<<OveralMaxSum(arr,num)<<endl;
     }
  }
