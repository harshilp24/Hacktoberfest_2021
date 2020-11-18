#Reference : https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:
            s = sorted(s)
            t = sorted(t)
            return s == t

print(isAnagram("tea", "eat"))
