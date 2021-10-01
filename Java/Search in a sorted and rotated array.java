import java.util.*;
class SearchinSortedandRotatedArray { //TIME COMPLEXITY 0(logn)
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("enter no of elements of array: ");
        in n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("enter array elements: ");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }    
        System.out.println("enter key: ");
        int key= sc.nextInt();
        int i= binarySearch(arr,0,n-1,key);
        if(i!=-1){
            System.out.println("key present at "+i+" postion.");
        }
        else{
            System.out.println("key not present.");
        } 
    }

    static int binarySearch(int arr[], int l,int h, int key){
        if(l>h){
            return -1;
        }
        int mid = (l+h)/2;

        
        if(arr[mid]==key){
            return mid;
        }
        if(arr[l]<=arr[mid]){ //SORTED
            if(key>=arr[l] && key<=arr[mid]){
                return binarySearch(arr, l,mid-1,key);
            }
            return binarySearch(arr,mid+1,h,key);
        }
        if(key>=arr[mid] && key<=arr[h]){
            return binarySearch(arr,mid+1,h,key);
        }
        return binarySearch(arr, l,mid-1,key);

    }
}

   
    

