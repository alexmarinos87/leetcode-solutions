class Solution(object):
    def convert(self, s, numRows):
        """
        Arrange the characters of the input string in a zigzag pattern on a given number of rows,
        then read row by row to form the output string.

        Approach:
        - Handle edge cases directly: If numRows is 1 or the string is shorter than numRows, return s.
        - Utilise a list to collect characters for each row.
        - Move down and up the rows in a controlled manner as you iterate over each character.

        Parameters
        ----------
        s : str
            Input string to be converted.
        numRows : int
            Number of rows in the zigzag pattern.

        Returns
        -------
        str
            The zigzag-converted string, read row by row.
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        step = -1  # Start by going downwards

        for char in s:
            rows[current_row] += char
            # Change direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                step *= -1
            current_row += step

        # Concatenate all rows to form the final string
        return ''.join(rows)
