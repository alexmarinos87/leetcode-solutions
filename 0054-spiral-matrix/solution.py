class Solution(object):
    def spiralOrder(self, matrix):
        """
        Spiral Matrix (LeetCode 54)

        Approach
        --------
        Boundary-tracking traversal (O(m*n)):
        - Maintain four boundaries: top, bottom, left, right.
        - Traverse:
            1) Top row left -> right, then top += 1
            2) Right column top -> bottom, then right -= 1
            3) Bottom row right -> left (if top <= bottom), then bottom -= 1
            4) Left column bottom -> top (if left <= right), then left += 1
        - Repeat until the boundaries cross. The guards prevent double-visiting
          when a single row or column remains.

        Parameters
        ----------
        matrix : List[List[int]]
            m x n grid of integers (m, n in [1, 10]).

        Returns
        -------
        List[int]
            Elements of `matrix` in spiral order.
        """
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # left -> right across the top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # top -> bottom down the right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # right -> left across the bottom row (if still valid)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # bottom -> top up the left column (if still valid)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res

