class Solution(object):
    def isAnagram(self, s, t):
        """
        Valid Anagram (LeetCode 242)

        Approach
        --------
        Frequency counting in O(n):
        - If lengths differ, they can't be anagrams.
        - Count chars in `s`, subtract with `t`; any negative means mismatch.
        - Works in O(n) time and O(1) extra space (since input is lowercase a–z).

        Parameters
        ----------
        s : str
            First string.
        t : str
            Second string.

        Returns
        -------
        bool
            True if `t` is an anagram of `s`; False otherwise.

        Follow-up
        ---------
        If inputs may contain Unicode, use a `collections.Counter` (hash map) instead
        of a fixed 26-length array; it generalizes to any characters.
        """
        if len(s) != len(t):
            return False

        counts = [0] * 26
        base = ord('a')

        for ch in s:
            counts[ord(ch) - base] += 1
        for ch in t:
            i = ord(ch) - base
            counts[i] -= 1
            if counts[i] < 0:
                return False

        return True

        # --- Unicode-friendly alternative ---
        # from collections import Counter
        # return Counter(s) == Counter(t)
