"""

Given 2 matrices, find the product.

Input Format

First line of input contains T - number of test cases. First line of each test case contains N1, M1 - size of the 1st matrix. Its followed by N1 lines each containing M1 intergers - elements of the 1st matrix. The next line contains N2, M2 - size of the 2nd matrix. Its followed by N2 lines each containing M2 intergers - elements of the 2nd matrix. Note that M1 = N2.

Constraints

1 <= T <= 100
1 <= N1,M1,N2,M2 <= 50
-100 <= mat[i][j] <= 100

Output Format

For each test case, print the resultant product matrix, separated by newline.

Sample Input 0

2
2 2
1 2 
3 -1 
2 3
1 -2 3 
2 3 -1 
2 3
27 29 53 
-28 49 -24 
3 4
23 52 -38 72 
-64 15 -59 -10 
-75 43 10 25 
Sample Output 0

5 4 1 
1 -9 10 
-5210 4118 -2207 2979 
-1980 -1753 -2067 -3106 

"""

test_cases = int(input())

def transpose(row, col, mat):
    trans = [[0 for i in range(row)] for j in range(col)]
    for i in range(row):
        for j in range(col):
            trans[j][i] = mat[i][j]
    return trans

def multiply(mat1, mat2):
    return sum([mat1[i]*mat2[i] for i in range(len(mat1))])

for i in range(test_cases):
    row1, col1 = map(int, input().split())
    mat1 = [list(map(int, input().split())) for i in range(row1)]
    row2, col2 = map(int, input().split())
    mat2 = [list(map(int, input().split())) for i in range(row2)]
    product = [[0 for i in range(col2)] for i in range(row1)]
    
    mat2 = transpose(row2, col2, mat2)
    
    for i in range(row1):
        for j in range(col2):
            product[i][j] = str(multiply(mat1[i], mat2[j]))
    
    for i in range(row1):
        print(' '.join(product[i]))
                               
                            
