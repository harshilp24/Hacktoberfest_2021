# NumPy Puzzle
#CUMMULATIVE SUM
def cumsum(l:list):
    if not l:
        return []
       
    sums = []
    sums.append(l[0])
   
    return helper(sums, l[1:])
   
    
def helper(sums:list, xs:list):
    if not xs:
        return sums
       
    s = sums[len(sums) - 1]
    sums.append(s + xs[0])
   
    if len(xs) > 1:
        return helper(sums, xs[1:])
   
    return sums
 
   
xs = [1]
print(cumsum(xs))
#[1]
xs = [1, 3, 3, 2, 5]
print(cumsum(xs))
# [1, 4, 7, 9, 14]
xs = [1, 1, 1, 2]
print(cumsum(xs))
# [1, 2, 3, 5]

#Explanation
#The functions in this puzzle compute a list of sums from the values of the input list. In the output list at index j there is the sum of sums[j-1] + input[j].
#This is done in a recursive way. The cumsum-function only starts the recursion by putting the first element of the input list in the first position of the output list and then it starts the recursion with the helper-function by passing the lists sums and xs[1:]. Note that in each recursion step the xs list is shorter because we slice off the first element each time.
#If xs was [] or [2] in the beginning we would get an exception. But it could easily be avoided by adding a check in each function. How would these checks look like?
#With the given input [1, 1, 1, 2] we compute the output [1, 1+1, 1+1+1, 1+1+1+2] = [1, 2, 3, 5]

