def find_pviot_index(A,start,end):
    pivot=A[end]
    p_index=start
    for iter in range(start,end):
        if A[iter] <= pivot:
            A[p_index],A[iter]=A[iter],A[p_index]
            p_index+=1
    A[p_index],A[end]=pivot,A[p_index]
    return p_index        

def quick_sort(A,start,end):
    if start < end:
        pivot_index=find_pviot_index(A,start,end)
        print("--------------",A)
        quick_sort(A,start,pivot_index-1)
        quick_sort(A,pivot_index+1,end)
        

#main
A=list()
n=int(input("Enter how many numbers you want ot enter: "))
for x in range(0,n):
    num=int(input("enter num:"))
    A.append(num)
print("Initial array:",A)     
quick_sort(A,0,n-1)
print("Sorted array :",A)
