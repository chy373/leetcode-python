'''
Problem: Power Of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Solution:
1. if it is power of 2(num&(num-1)=0)
2. get rid of numbers that is power of 2 but not power of 4(check if 1 is located in odd position)

0x5555555555555555 =- 0b101010101010101010101010101010101010101
'''


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num & (num - 1) == 0 and num & 0x5555555555555555 == num
