#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_water=0
        while(left<right):
            width=right-left
            curr_area=min(height[left],height[right])*width
            if(curr_area>max_water):
                max_water=curr_area
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return max_water

        
