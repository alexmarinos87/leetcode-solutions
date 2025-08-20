from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        Approach: Count letters (26 bucket array) → use the 26-tuple as dict key.
        Complexity: Time O(N*K), Space O(N)
        """
        groups = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - 97] += 1
            groups[tuple(freq)].append(s)
        return list(groups.values())
