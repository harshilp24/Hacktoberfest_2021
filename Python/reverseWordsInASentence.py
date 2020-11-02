
#Reference : https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords(s: str) -> str:
        
        sList = list(map(str, s.split()))
        revList = sList[::-1] 
        rev = " ".join(s for s in revList)
        return rev

print(reverseWords("The words in this sentence will be reversed"))
