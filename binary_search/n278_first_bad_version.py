import random
'''
278. First Bad Version Add to List
Difficulty: Easy Tags: Binary Search

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return random.choice([False, True])


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        #  关于right的赋值
        #  right = n-1 => while(left <= right) => right = middle-1;
        #  right = n => while(left < right) => right = middle;
        # 换言之，算法所操作的区间,是左闭右开区间,还是左闭右闭区间,这个区间,需要在循环初始化。
        # 且在循环体是否终止的判断中,以及每次修改left, right区间值这三个地方保持一致,否则就可能出错
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left
