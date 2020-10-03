#sort to implement bucket sort also requires a insertion sort

#insertion sort
def insertionSort(subArray):
    for i in range(1, len(subArray)):
        up = subArray[i]
        j = i - 1
        while j >= 0 and subArray[j] > up:
            subArray[j + 1] = subArray[j]
            j -= 1
        subArray[j + 1] = up
    return subArray

#bucket sort
def bucketSort(array):
    arr = []
    slot_num = 10 # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

        # Put array elements in different buckets
    for j in array:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

        # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

        # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            array[k] = arr[i][j]
            k += 1
    return array

# Driver Code
array = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434, 0.234]
print("Sorted Array is")
print(bucketSort(array))
