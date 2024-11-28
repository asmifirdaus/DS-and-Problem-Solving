#https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        print(a,len(a))
        if(len(a)!=len(nums)):
            return True
        return False
