#https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=ddict(s)
        print(a)
        b=dict(t)
        if(a==b):
            return true
        else:
            return false
