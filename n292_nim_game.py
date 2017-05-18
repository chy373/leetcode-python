'''
Problem:
You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
'''

'''
Solution:
there is a more complicate problem in the book named beauty of coding.
reference it for more.
'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0

if __name__ == '__main__':
    s = Solution()
    print s.canWinNim(5)
