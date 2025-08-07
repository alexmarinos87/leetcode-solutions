class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Return the length of the last word in the given string.

        Strategy:
        - Strip trailing spaces.
        - Split the string into words.
        - Return the length of the last word.

        Parameters
        ----------
        s : str
            Input string containing words and spaces.

        Returns
        -------
        int
            Length of the last word in s.
        """
        # Remove trailing spaces and split by whitespace
        words = s.strip().split()
        return len(words[-1])
