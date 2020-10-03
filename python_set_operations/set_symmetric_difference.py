'''
this script shows the symmetric difference of two sets
'''

set_A = {1,2,3,4,5,6}
set_B = {5,6,7,8,9,10}

print("A symmetric difference B is : ",end = " ")
print(set_A.symmetric_difference(set_B))

print("B symmetric difference A is : ",end = " ")
print(set_B.symmetric_difference(set_A))