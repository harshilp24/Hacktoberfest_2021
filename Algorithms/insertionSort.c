#include<stdio.h>
void insertionSort(int array[], int length){
    
    for(int i = 1 ; i < length; i++){
        int currKey = array[i];
        int j = i;
        // check whether the next position is greater than currkey
        while(j >0 && array[j-1]>currKey){
            array[j] = array[j-1];
            j--;
        }
        // ficxing the jth position
        array[j] = currKey;
    }
    // prting out 
    for(int i = 0; i < length; i++){
        printf(" %d ", array[i]);
    }

}
int main (void){
    int array[] = {1,67,35,90,4567,13,0,5,8,56};
    int length = sizeof(array)/sizeof(array[0]);
    insertionSort(array, length);
    
    return 0;
}