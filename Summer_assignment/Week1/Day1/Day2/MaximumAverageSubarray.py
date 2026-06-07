class Solution(object):
  def findMaxAverage(self, nums, k):

    FirstSum = sum(nums[:k])
    MaxSum = FirstSum
    for i in range(k, len(nums)):
        FirstSum += nums[i] - nums[i - k]
        MaxSum = max( MaxSum, FirstSum)
    return float( MaxSum) / k
                                                                