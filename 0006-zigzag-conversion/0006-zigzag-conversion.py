class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        Approach: Row simulation with direction toggle.
        Why it fits: The zigzag just walks row indices 0..numRows-1 and back; append each character to the active row then flip direction at the top/bottom.
        Correctness: Each character is appended to exactly the row it occupies in the zigzag traversal; concatenating rows yields the required reading order.
        Complexity: Time O(n), Space O(n) for the row buffers.
        """
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        rows = [''] * numRows
        r, dr = 0, 1 # current row, direction (+1 down, -1 up)
        for ch in s:
            rows[r] += ch
            if r == 0: dr = 1
            elif r == numRows - 1: dr = -1
            r += dr
        return ''.join(rows)