class Solution(object):
    def minWindow(self, s, t):
        """
        Minimum Window Substring (LeetCode 76)

        Approach
        --------
        Sliding window with frequency matching (O(m + n)):
        - Count required characters in `t` with a Counter `need`.
        - Expand the right end of the window over `s`, tracking counts in `window`.
        - Maintain `have`: number of characters whose window count meets `need`.
        - Once `have == len(need)`, shrink from the left to find the smallest valid window,
          updating the best answer along the way.
        - Because each index moves at most once, the total time is linear.

        Parameters
        ----------
        s : str
            Source string to search.
        t : str
            Multiset of required characters (duplicates matter).

        Returns
        -------
        str
            The smallest substring of `s` containing all characters of `t` (with multiplicity),
            or "" if no such window exists.
        """
        if not s or not t or len(t) > len(s):
            return ""

        from collections import Counter

        need = Counter(t)
        required = len(need)  # number of distinct chars to satisfy
        window = {}

        have = 0
        best_len = float('inf')
        best_l, best_r = 0, 0

        l = 0
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Try to shrink while valid
            while have == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l, best_r = l, r + 1  # r is inclusive

                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                l += 1

        return s[best_l:best_r] if best_len != float('inf') else ""

