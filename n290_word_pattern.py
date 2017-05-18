'''
Problem:
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Solution:
my solution is use a hash table to keep the relation between pattern and str at the same index,
after the has table is created, check if different keys map to the same value
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        res = {}
        res1 = {}
        if len(words) != len(pattern):
            return False
        else:
            for i in range(len(words)):
                if res.get(pattern[i]) is None:
                    res[pattern[i]] = words[i]
                elif res.get(pattern[i]) != words[i]:
                    return False
            for k, v in res.items():
                res1[v] = k
            if len(res) == len(res1):
                return True
            else:
                return False

if __name__ == '__main__':
    s = Solution()
    print s.wordPattern('abab', 'dog dog dog dog')
