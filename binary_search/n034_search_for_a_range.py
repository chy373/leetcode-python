'''
34. Search for a Range Add to List
Difficulty: Medium Tags: Binary Search Array

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # use binary_search twice
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        res = [-1, -1]
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return res
        res[0] = left
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) / 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res[1] = right
        return res
