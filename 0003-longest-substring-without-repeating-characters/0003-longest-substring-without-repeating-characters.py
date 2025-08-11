class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Longest Substring Without Repeating Characters (LeetCode 3)

        Approach
        --------
        Sliding window with last-seen indices (O(n)):
        - Maintain a window [left, right] containing unique chars.
        - Keep a dict `last` mapping char -> last index seen.
        - When s[right] repeats within the window, move `left` to last[char] + 1.
        - Update the best window length each step.
        - Time: O(n), Space: O(min(n, charset)).

        Parameters
        ----------
        s : str
            Input string (may include letters, digits, symbols, and spaces).

        Returns
        -------
        int
            Length of the longest substring without repeating characters.
        """
        last = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)

        return best
