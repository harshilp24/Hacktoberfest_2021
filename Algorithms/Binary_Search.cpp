//Binary Search is used only for sorted array.

//Iteraive Solution ---- This is best method because it has O(logN) time complexity and O(1) space complexity
#include <iostream>
using namespace std;

int search(int arr[], int size, int item)
{
    int start = 0;
    int end = size - 1;
    while (end >= start)
    {
        int mid = (start + end) / 2;
        if (item == arr[mid])
            return mid;
        else if (item > arr[mid])
            start = mid + 1;
        else
            end = mid - 1;
    }
    return -1;
}

int main()
{
    int n, item;
    cout << "Enter the size of array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Enter the item to search: ";
    cin >> item;
    cout << "Element is found at index " << search(arr, n, item);
    return 0;
}


// Recursive Solution --- Even if it's time complexity is O(logN), it is not the best method because its space complexity is O(logN).

// #include <iostream>
// using namespace std;

// int search(int arr[], int start, int end, int item)
// {
//     if (start > end)
//         return -1;
//     int mid = (start + end) / 2;
//     if (arr[mid] == item)
//         return mid;
//     else if (arr[mid] < item)
//         search(arr, start + 1, end, item);
//     else
//         search(arr, start, end - 1, item);
// }
// int main()
// {
//     int n, item;
//     cout << "Enter the size of array: ";
//     cin >> n;
//     int arr[n];
//     cout << "Enter the elements of the array: ";
//     for (int i = 0; i < n; i++)
//     {
//         cin >> arr[i];
//     }
//     cout << "Enter the item to search: ";
//     cin >> item;
//     cout << "Element is found at index " << search(arr, 0, n - 1, item);
//     return 0;
// }
