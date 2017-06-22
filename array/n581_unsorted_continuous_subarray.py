'''
581. Shortest Unsorted Continuous Subarray Add to List

Difficulty: Easy Tags: Array
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''


class Solution(object):

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref = sorted(nums)
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            if nums[l] != ref[l]:
                res.append(l)
            if nums[r] != ref[r]:
                res.append(r)
            l += 1
            r -= 1
        if not res:
            return 0
        else:
            return max(res) - min(res) + 1

# The idea behind this method is that the correct position of the minimum element in the unsorted subarray helps to determine the required left boundary.
# Similarly, the correct position of the maximum element in the unsorted subarray helps to determine the required right boundary.
    def findUnsortedSubarray1(self, nums):
        pass
