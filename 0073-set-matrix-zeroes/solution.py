class Solution(object):
    def setZeroes(self, matrix):
        """
        Set Matrix Zeroes (LeetCode 73)

        Approach
        --------
        In-place markers with first row/column (O(m*n) time, O(1) extra space):
        - Use the first row and first column as marker arrays: if matrix[r][c] == 0,
          mark matrix[r][0] = 0 and matrix[0][c] = 0.
        - Keep two booleans to remember whether the original first row or first column
          should be zeroed (since they double as markers).
        - After marking, zero cells whose row or column is marked.
        - Finally, zero the first row/column if their booleans are set.

        Parameters
        ----------
        matrix : List[List[int]]
            m x n integer matrix to modify in-place.

        Returns
        -------
        None
            Modifies `matrix` in-place; does not return a value.
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])

        # Check if first row/col need to be zeroed
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))

        # Use first row and column as markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero cells based on markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero first row/column if needed
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0

        # In-place; no return value.
        # --- Simpler alternative (O(m+n) extra space) ---
        # rows, cols = set(), set()
        # for r in range(m):
        #     for c in range(n):
        #         if matrix[r][c] == 0:
        #             rows.add(r); cols.add(c)
        # for r in range(m):
        #     for c in range(n):
        #         if r in rows or c in cols:
        #             matrix[r][c] = 0

