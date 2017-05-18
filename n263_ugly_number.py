'''
Problem:
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

Solution: divide a number with 2, 3, 5 until it cannot divided by them, if num becomes 1, it's ugly
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num%i == 0:
                num = num/i
        if num == 1:
            return True
        else:
            return False

