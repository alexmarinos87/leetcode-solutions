class Solution(object):
    def rotate(self, matrix):
        """
        Rotate Image (LeetCode 48)

        Approach
        --------
        Transpose + reverse rows (in-place, O(n^2) time, O(1) extra space):
        - Transpose: swap matrix[i][j] with matrix[j][i] for all i < j.
        - Reverse each row.
        This sequence rotates the matrix 90 degrees clockwise without extra storage.

        Parameters
        ----------
        matrix : List[List[int]]
            Square n x n matrix to rotate in-place.

        Returns
        -------
        None
            Modifies `matrix` in-place; does not return a value.
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

        # No return; in-place modification.
        # --- Alternative (4-way swap) ---
        # for layer in range(n // 2):
        #     first, last = layer, n - 1 - layer
        #     for i in range(first, last):
        #         offset = i - first
        #         top = matrix[first][i]
        #         # left -> top
        #         matrix[first][i] = matrix[last - offset][first]
        #         # bottom -> left
        #         matrix[last - offset][first] = matrix[last][last - offset]
        #         # right -> bottom
        #         matrix[last][last - offset] = matrix[i][last]
        #         # top -> right
        #         matrix[i][last] = top

