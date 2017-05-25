'''
136. Single Number Add to List
Difficulty: Easy Tags: Hash Table, Bit Manipulation

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Subscribe to see which companies asked this question.

'''
import operator


class Solution(object):

    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key

    # A^A = 0 A^0 = A
    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber3(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber(self, nums):
        return reduce(operator.xor, nums)
