class Solution(object):
    def isValidSudoku(self, board):
        """
        Valid Sudoku (LeetCode 36)

        Approach
        --------
        Sets per row, column, and 3x3 box (O(1) time & space on fixed 9x9 grid):
        - Iterate each cell; skip '.'.
        - If a digit is already present in its row, column, or box set, the board is invalid.
        - Otherwise add it to the corresponding sets and continue.
        - Box index is computed as (r // 3) * 3 + (c // 3).

        Parameters
        ----------
        board : List[List[str]]
            9x9 grid of characters '1'..'9' or '.' for empty.

        Returns
        -------
        bool
            True if the filled cells obey Sudoku rules; False otherwise.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 0..8

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue

                b = (r // 3) * 3 + (c // 3)
                if (ch in rows[r]) or (ch in cols[c]) or (ch in boxes[b]):
                    return False

                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)

        return True

