#Python program to implement pigeonHole sort
#It is not much used but where the range is same as the no number of keys it can be preferred over bubble sort
#complexity is O(n + Range)

def pigeonHoleSort(array):
    #size of range of values in the list(no of pigeon holes)
    min_no = min(array)
    max_no = max(array)
    size = max_no + min_no + 1

    #pigeon holes created with default value 0
    pholes = [0] * size

    #putting pigeon in there specific holes
    for x in array:
        pholes[x - min_no] += 1

    i = 0

    #now put them back in the array
    for count in range(size):
        while pholes[count] > 0:
            pholes[count] -= 1
            array[i] = count + min_no
            i +=1

array = [10,3,5,17,15,13,10,2]
print("Sorted order is : ")

pigeonHoleSort(array)

for i in range(0, len(array)):
    print(array[i])




