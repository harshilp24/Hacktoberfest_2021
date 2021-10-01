import java.util.*;
class SearchinSortedandRotatedArray { //TIME COMPLEXITY 0(logn)
    public static void main(String[] args){
        int arr[] = {4,5,6,1,2};
        int n = arr.length;
        Scanner sc = new Scanner(System.in);
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

   
    

