#!/usr/bin/env python
# encoding: utf-8

'''
13. Roman to Integer
Difficulty:Easy Tags: Math String
DescriptionHintsSubmissionsSolutions
Discuss   Editorial Solution Pick One
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

# roman -- int I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)
# V L D can't be substracted


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s[::-1]:
            if i == 'I':
                if res < 5:
                    res += 1
                else:
                    res -= 1
            if i == 'V':
                res += 5
            if i == 'X':
                if res < 50:
                    res += 10
                else:
                    res -= 10
            if i == 'L':
                res += 50
            if i == 'C':
                if res < 500:
                    res += 100
                else:
                    res -= 100
            if i == 'D':
                res += 500
            if i == 'M':
                res += 1000
        return res
