'''
1. Two Sum Add to List
Difficulty: Easy Tags: Array Hash Table

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
Subscribe to see which companies asked this question.

'''


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ref = {}
        for idx, i in enumerate(nums):
            if target - i not in ref:
                ref[i] = idx
            else:
                return [ref[target - i], idx]
