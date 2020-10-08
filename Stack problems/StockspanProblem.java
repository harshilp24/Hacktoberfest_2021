import java.util.*; 
class StockspanProblem { 
static void printNGE(int arr[], int n,int arr1[]) 
{ 
	Stack<Integer> s = new Stack<Integer>(); 

        arr1[0]=1;

	for (int i = 0; i<n; i++) 
	{ 

		while (!s.empty() && arr[s.peek()] <= arr[i]) 
               {
		s.pop();
                }
	
              arr1[i]= (s.empty())?(i+1):(i-s.peek()); 
               
		s.push(i);

	} 

} 
static void printArray(int arr[])
{
System.out.print(Arrays.toString(arr));
}


public static void main(String[] args) 
{ 
	Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int[] arr=new int[n];
for(int i=0;i<n;i++)
{
arr[i]=sc.nextInt();
}
int arr1[] = new int[n];
	printNGE(arr, n,arr1); 
printArray(arr1);
} 
} 
