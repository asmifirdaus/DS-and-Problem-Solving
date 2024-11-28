#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        start=0
        res=0
        for end in range(len(s)):
            if s[end] in seen:
                start=max(start,seen[s[end]]+1) 
            seen[s[end]]=end
            res=max(res,end-start+1)
        return res
