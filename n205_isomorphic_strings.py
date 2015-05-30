#Given two strings s and t, determine if they are isomorphic, assume two strings have the same length
# isisomorphic1 get an error when occuring situations "ab" "bb" and it's ugly to use count, it's not neccessary
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic1(self, s, t):
        hash = {}
        count = 0
        for i in range(len(s)):
            if not hash.get(s[i]):
                hash[s[i]] = t[i]
            else:
                if hash[s[i]] != t[i]:
                    count -= 1
            count += 1
        if count == len(s):
            return True
        else:
            return False

    def isIsomorphic2(self, s, t):
        res = {}
        for i in xrange(len(s)):
            if s[i] in res:
                if res[s[i]] != t[i]:
                    return False
            else:
                if t[i] in t[:i]:
                    return False
                res[s[i]] = t[i]
        return True

    def isIsomorphic3(self,s ,t):
        def temp_func(s, t):
            res = {}
            for i in xrange(len(s)):
                if s[i] not in res:
                    res[s[i]] = t[i]
                else:
                    if res[s[i]] != t[i]:
                        return False
            return True
        return temp_func(s, t) and temp_func(t, s)


if __name__ == '__main__':
    sol = Solution()
    s = 'ab'
    t = 'aa'
    print sol.isIsomorphic1(s, t)
    print sol.isIsomorphic2(s, t)
    print sol.isIsomorphic3(s, t)
