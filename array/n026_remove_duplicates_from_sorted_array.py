'''
26. Remove Duplicates from Sorted Array Add to List
Difficulty: Easy Tags: Array Two Pointers

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # put the nth number in nth place
        prev = None
        idx = 0
        for i in nums:
            if i != prev:
                nums[idx] = i
                prev = i
                idx += 1
        return idx


if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([])
