"""
217. Contains Duplicate
Difficulty: Easy tags: Array HashTable

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))

if __name__ == "__main__":
    s = Solution()
    s.containsDuplicate([1, 2, 45, 2])
