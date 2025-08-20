class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Approach: Sliding window with counts (or last-seen indices). Expand right; while duplicate appears, move left until the window is valid again.
        Why it fits: We need a maximal window under a "no duplicates" constraint-classic sliding window.
        Invariants: For all chars in s[left:right + 1], count[c] <= 1; best tracks the max length.
        Correctness: Every time a duplicate would violate the constraint, we shrink to restore validity, so every valid maximal window is considered.
        Complexity: Time O(n), Space O(n)
        """
        from collections import defaultdict
        count = defaultdict(int) # any new key automatically has value 0
        left = 0 # start of sliding window
        best = 0 # length of the longest valid substring
        for right, ch in enumerate(s): # right is the index were expanding; ch is the current character
            count[ch] += 1 # we add the character to our count dictionary
            while count[ch] > 1: # resolve duplicate
                count[s[left]] -= 1 # decrease character count since we are shrinking window
                left += 1 # shrink window from left side
            best = max(best, right - left +1) # Checking if current window is longest so far; right - left + 1 is the length of the window inclusive of both ends
        return best
