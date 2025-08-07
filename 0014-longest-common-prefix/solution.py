class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Find the longest common prefix among a list of strings.

        Strategy:
        - Compare characters of all strings one by one (column by column).
        - Stop at the first mismatch or at the end of any string.

        Parameters
        ----------
        strs : List[str]
            List of lowercase English strings.

        Returns
        -------
        str
            The longest common prefix, or "" if none exists.
        """
        if not strs:
            return ""
        
        # Take the first string as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                # If index out of bounds or mismatch, return prefix up to i
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]

