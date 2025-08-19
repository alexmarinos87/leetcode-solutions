class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        Approach: Naive window comapre. Slide a window of length m and compare.
        Correctness: If haystack[i:i+m] == needle, i is the first index by iteration order.
        Complexity: Time O(n*m) (slicing/compare), Space O(1) extra.
        """
        if needle == "":
            return 0
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
