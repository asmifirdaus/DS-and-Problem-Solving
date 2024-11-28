#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        start_num=None
        max_len=0
        for num in nums:
            if num-1 not in num_set:
                current_num=num
                current_len=1
                while current_num+1 in num_set:
                    current_num+=1
                    current_len+=1
                if current_len>max_len:
                    max_len=current_len
                    start_len=num
        return max_len
        
