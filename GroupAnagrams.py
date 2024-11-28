#https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di={}
        for i in strs:
            sortedstr=''.join(sorted(i))
            if sortedstr in di:
                di[sortedstr].append(i)
            else:
                di[sortedstr]=[i]
        return list(di.values())
