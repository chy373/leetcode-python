'''
231. Power of Two Add to List
Difficulty: Easy Tags: Math Bit Manipulation

Given an integer, write a function to determine if it is a power of two.
'''


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return not (n & (n - 1))
