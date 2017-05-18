#!/usr/bin/env python

import heapq
from itertools import chain
from collections import Counter


class Solution(object):

    """Docstring for Solution. """

    def topK_frequent(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: list[int]
        """
        result = [i[0] for i in Counter(nums).most_common(k)]
        return result

    # bucket sort
    def topK_frequent1(self, nums, k):
        bucket = [[] for i in range(len(nums))]
        for num, freq in Counter(nums).iteritems():
            bucket[len(nums) - freq].append(num)
        return list(chain(*bucket))[:k]

    # heap queue

if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 3, 4, 4]
    s = Solution()
    print s.topK_frequent(nums, 2)
    print s.topK_frequent1(nums, 2)
