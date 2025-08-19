class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Approach: Horizontal scan. Start with prefix = strs[0]; for each next string, shrink prefix while it isn't a prefix of that string.
        Correctness: The LCP of all strings equals the LCP of (current LCP, next string) iteratively; shrinking stops exactly at the maximal common prefix.
        Complexity: Time O(S) total (each char compared at most once across shrinks), Space O(1)
        """
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix