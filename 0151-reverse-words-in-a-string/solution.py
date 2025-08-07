class Solution(object):
    def reverseWords(self, s):
        """
        Reverse the order of words in the input string.

        Strategy:
        - Use split() to separate words, which automatically removes extra spaces.
        - Reverse the list of words.
        - Join the words with a single space.

        Parameters
        ----------
        s : str
            Input string with words and spaces.

        Returns
        -------
        str
            Words in reversed order, separated by single spaces, with no extra spaces.
        """
        # Split by whitespace, reverse the list, and join by single space
        return " ".join(s.split()[::-1])

