class Solution(object):
    def strStr(self, haystack, needle):
        """
        Locate the index of the first occurrence of 'needle' within 'haystack'.

        Approach:
        - If 'needle' is empty, return 0 immediately—by definition.
        - Utilise Python’s built-in string search capability for optimal clarity and efficiency.
        - If not found, return -1.

        Parameters
        ----------
        haystack : str
            The main string in which to search.
        needle : str
            The substring to locate.

        Returns
        -------
        int
            The index of the first occurrence of 'needle' in 'haystack', or -1 if absent.
        """
        if needle == "":
            return 0
        return haystack.find(needle)

