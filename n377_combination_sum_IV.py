#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    """Docstring for Solution. """

    def combination_sum_IV(self, nums, target):
        """Docstring for combination_sum_IV, recursive version

        :type nums: list[int]
        :type target: int
        :rtype: int

        """
        count = 0
        if target == 0:
            return 1
        for n in nums:
            if target >= n:
                count += self.combination_sum_IV(nums, target - n)
        return count

    def combination_sum_IV_1(self, nums, target):
        """
        Docstring for combination_sum_IV_1, storge immediate data.
        """
        dp = [1] + [0] * target

        def helper(nums, target):
            if dp[target] != 0:
                return dp[target]
            count = 0
            for n in nums:
                if target >= n:
                        count += helper(nums, n)
            return count
        return helper(nums, target)

    def combination_sum_IV_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        start = min(nums)
        if start > target:
            return 0
        # record number of combinations for i
        dp = [1] + [0] * target
        for i in range(len(dp)):
            # skip numbers that have no combinations
            if dp[i] != 0:
                for n in nums:
                    if i + n < len(dp):
                        dp[i + n] += dp[i]
        return dp[-1]

    def combination_sum_IV_3(self, nums, target):
        dp = [1]
        for i in xrange(1, target + 1):
            dp.append(sum(dp[i-n] for n in nums if i-n >= 0))
        return dp[-1]


if __name__ == "__main__":
    import time
    s = Solution()
    nums = [2, 3]
    target = 100
    print '--- start1 ---'
    t1 = time.time()
    print s.combination_sum_IV_3(nums, target)
    t2 = time.time()
    print '--- cost1 ---'
    print t2 - t1
    print '--- start2 ---'
    print s.combination_sum_IV_2(nums, target)
    t3 = time.time()
    print '--- cost2 ---'
    print t3 -t2
