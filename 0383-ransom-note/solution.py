class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        Ransom Note (LeetCode 383)

        Approach
        --------
        Frequency counting (O(n)):
        - Count letters in `magazine` (only 'a'..'z', per constraints).
        - For each char in `ransomNote`, decrement its count.
        - If any count drops below zero, magazine lacks enough of that letter → return False.
        - Otherwise, all letters are available → return True.
        - Early exit: if ransomNote is longer than magazine, it can't be constructed.

        Parameters
        ----------
        ransomNote : str
            The required note consisting of lowercase letters.
        magazine : str
            The available letters, each usable at most once.

        Returns
        -------
        bool
            True if `ransomNote` can be constructed from `magazine`; False otherwise.
        """
        if len(ransomNote) > len(magazine):
            return False

        counts = [0] * 26
        base = ord('a')

        for ch in magazine:
            counts[ord(ch) - base] += 1

        for ch in ransomNote:
            i = ord(ch) - base
            counts[i] -= 1
            if counts[i] < 0:
                return False

        return True

        # --- Alternative (concise) ---
        # from collections import Counter
        # return not (Counter(ransomNote) - Counter(magazine))

