'''
20. Valid Parentheses Add to List
Difficulty: Easy Tags: Stack String

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            if i in pairs.values():
                try:
                    top = stack.pop()
                except:
                    return False
                if pairs[top] != i:
                    return False
        if stack:
            return False
        else:
            return True
