class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        Approach: Split on whitespace, reverse the list, join with single spaces.
        Why it fits: split() collapses multiple spaces and trims ends automatically.
        Correctness: Words are tokens produced by split(); reverse that sequence and joining with ' ' yields the required order with a single space between words.
        Complexity: Time O(n), Space O(n) for token list.
        """
        return ' '.join(reversed(s.split()))