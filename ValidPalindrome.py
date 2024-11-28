#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[val.lower() for val in s if val.isalnum()]
        if(l==l[::-1]):
            return True
        return False
                
