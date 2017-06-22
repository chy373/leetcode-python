#!/usr/bin/env python
# encoding: utf-8

'''
14. Longest Common Prefix
Difficulty:Easy Tags: String

Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):

    # my ugly solution
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        l = len(strs[0])
        prefix = ''
        for s in strs:
            l = min(l, len(s))

        for i in range(l):
            prev = strs[0][i]
            for s in strs:
                if s[i] != prev:
                    return prefix
            prefix += prev
        return prefix

    # @return a string
    # nice solution with zip
    # for-else syntax
    def longestCommonPrefix1(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

    # reduce function learn from discuss
    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i + 1
            else:
                break
        return str1[:i]

    # @return a string
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp, strs)

if __name__ == "__main__":
    s = Solution()
    print s.longestCommonPrefix(['a'])
