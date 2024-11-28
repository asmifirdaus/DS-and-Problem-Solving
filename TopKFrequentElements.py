#https://leetcode.com/problems/top-k-frequent-elements/

import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fm=Counter(nums)
        topk=heapq.nlargest(k, fm.keys(),key=fm.get)
        return topk
        
