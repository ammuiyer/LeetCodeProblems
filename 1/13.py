# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j]==target):
                    ans.append(i)
                    ans.append(j)
                    return ans

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums)
            
            
