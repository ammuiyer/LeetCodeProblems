#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        sum = 0
        for i in range(0, len(nums)):
            sum = sum+nums[i]
            ans.append(sum)
        return ans