"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and
make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        lines = [[] for _ in range(numRows)]
        i = 0
        try:
            while 1:
                for line in lines:
                    line.append(s[i])
                    i += 1
                for line in lines[-2:0:-1]:
                    line.append(s[i])
                    i += 1
        except IndexError:
            return ''.join(''.join(line) for line in lines)

if __name__ == '__main__':
    sol = Solution()
    s = 'abcdefghijk'
    print sol.convert(s, 2)
    print sol.convert(s, 5)
