class Solution(object):
  def maxSubArray(self, nums):
    maxSum=nums[0]
    currentSum=0
    for num in nums:
        currentSum+=num
        maxSum=max(maxSum,currentSum)
        if currentSum<0:
            currentSum=0
    return maxSum