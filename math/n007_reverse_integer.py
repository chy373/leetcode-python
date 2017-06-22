'''
7. Reverse Integer
DescriptionHintsSubmissionsSolutions
Total Accepted: 244193
Total Submissions: 1010260
Difficulty: Easy
Contributor: LeetCode
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

spoilers:
Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

Subscribe to see which companies asked this question.

Hide Tags Math
Show Similar Problems
'''


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 2**31 - 1
        MIN = -2**31

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        res = 0
        while x != 0:
            # divmod()
            res = res * 10 + x % 10
            x = x / 10
            if res * sign > MAX or res * sign < MIN:
                return 0
        return res * sign

if __name__ == "__main__":
    s = Solution()
    print s.reverse(-123)
