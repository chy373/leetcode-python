'''
191. Number of 1 Bits Add to List
Difficulty: Easy Tags: Bit Manipulation

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

'''


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        w = 0
        for i in range(32):
            if n & 1 == 1:
                w += 1
            n >>= 1
        return w

    # Using bit operation to cancel a 1 in each round
    # Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just cancel the last 1
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
