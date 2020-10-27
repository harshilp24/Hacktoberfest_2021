"""
To know about collatzsequence:[Click here](https://esolangs.org/wiki/Collatz_sequence) 
"""
def getCollatzSequence(x):
    
    while x > 1:
      print(x,end='')
      if(x%2 != 0):
         x = 3*x + 1
      else:
         x = x//2
    print(1,end='')

n = int(input('Enter number: '))
print('sequence: ',end='')
getCollatzSequence(n)   
	  

		


