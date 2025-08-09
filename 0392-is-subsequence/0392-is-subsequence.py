class Solution(object):
    def isSubsequence(self, s, t):
        """
        Determine if string 's' is a subsequence of string 't'.

        Approach:
        - Use two pointers: one for 's', one for 't'.
        - Advance the 't' pointer on every iteration.
        - Advance the 's' pointer only when matching characters are found.
        - If the 's' pointer reaches the end of 's', it is a subsequence.

        Parameters
        ----------
        s : str
            The string we are checking as a potential subsequence.
        t : str
            The reference string.

        Returns
        -------
        bool
            True if 's' is a subsequence of 't', False otherwise.
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
