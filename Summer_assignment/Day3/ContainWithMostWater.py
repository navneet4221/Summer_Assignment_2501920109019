class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        AREA = 0
        while left < right: 
            width = right - left
            area = min(height[left], height[right]) * width
            AREA = max(AREA, area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return AREA
