#include<stdio.h>
#include<math.h>
int lastmin(int arr[],int segment_tree[],int i,int size)
{
    int p=0;
    while(p<size-1)
    {
        if(arr[segment_tree[2*p+2]]<=arr[i])
            p=2*p+2;
        else    
            p=2*p+1;
    }
    return p-size+1;
}
int nextrightmin(int arr[],int segment_tree[],int i,int size)
{
    int p=0,s=0,e=size-1,j=size;
    while(p<size-1)
    {
        int m=(s+e)/2;
        if(i<m)
        {
            if(arr[segment_tree[2*p+2]]<arr[i])
                j=2*p+2;
            p=2*p+1;
            e=m;
        }
        else    
            p=2*p+2;
            s=m+1;
    }
    while(j<size-1)
    {
        if(arr[segment_tree[2*j+1]]<arr[i])
            j=2*j+1;
        else    
            j=2*j+2;
    }
    return j-size+1;
}
int rmq(int segment_tree[],int arr[],int i,int j,int s,int e,int p)
{

    if(j<s || i>e)
        return e+1;
    if(i<=s && e<=j)
        return segment_tree[p];
    int mid=(s+e)/2;
    int l1 = rmq(segment_tree,arr,i,j,s,mid,2*p+1);
    int l2 = rmq(segment_tree,arr,i,j,mid+1,e,2*p+2);
    if(arr[l1]<arr[l2])
        return l1;
    else 
        return l2;
}
void buildtree(int segment_tree[],int arr[],int l,int size)
{
    for(int i=0;i<size;i++)
        segment_tree[size+i-1]=i;
    for(int i=size-2;i>=0;i--)
        {
            if(arr[segment_tree[2*i+1]]>arr[segment_tree[2*i+2]])
                segment_tree[i]=segment_tree[2*i+2];
            else
                segment_tree[i]=segment_tree[2*i+1];
        }
}
void update(int arr[],int k, int x, int segment_tree[],int size)
{
    int count=0;
    int p=k;
    arr[p]=x;
    p=(size-1+p-1)/2;
    while(p>=0)
    {
        if(arr[segment_tree[2*p+1]]>arr[segment_tree[2*p+2]])
            segment_tree[p]=segment_tree[2*p+2];
        else
            segment_tree[p]=segment_tree[2*p+1];
        
        p = ((p-1)/2);
        if(p==0)
            count++;
        if(count==2)
            break;
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    int a[n];
     for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    float value;
    int size;
    value=(log(n)/log(2));
    int p=value/1;
    if(value-p == 0)
        size=n;
    else
        size= pow(2,p+1);
    int arr[size+1];
    arr[size]=pow(2,30)-1; //for rmq
    for(int i=0;i<n;i++)
        arr[i]=a[i];
    for(int i=n;i<size;i++)
        arr[i]=pow(2,30)-1;
    int l=2*size-1;
    int segment_tree[l];
    buildtree(segment_tree,arr,l,size);
    printf("THE SEGMENT TREE ARRAY IS-->");
    for(int i=0;i<l;i++)
        printf("%d ",segment_tree[i]);
    int x,k,A,B;
    printf("\nenter the index of the number which you want to update-->");
    scanf("%d",&k);
    printf("enter new number to be updated at index %d-->",k);
    scanf("%d",&x);
    a[k]=x;
    update(arr,k,x,segment_tree,size);
    printf("the updated segment tree array is--> ");
    for(int i=0;i<l;i++)
        printf("%d ",segment_tree[i]);
    printf("\nENTER RANGE is from ");
    scanf("%d %d",&A,&B);
    int ans=rmq(segment_tree,arr,A,B,0,size-1,0);
    printf("%d",ans);
    printf("ENTER THE INDEX FOR WHICH U WANT NEXT RIGHT MINIMUM-->");
    int t;
    scanf("%d",&t);
    int output = nextrightmin(arr,segment_tree,t,size); 
    printf("%d",output);
    int h;
    printf("enter the dfghn");
    scanf("%d",&h);
    int output1=lastmin(arr,segment_tree,h,size);
    printf("%d",output1);
    return 0;

}
