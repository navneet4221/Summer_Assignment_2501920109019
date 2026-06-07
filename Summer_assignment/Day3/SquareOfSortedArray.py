class Solution:
    def sortedSquares(self, nums):
        s = [x * x for x in nums]
        s.sort()
        return s
