class Solution(object):
    def isAnagram(self, s, t):
        """
        Approach: Fixed-size frequency array of 26 letters.
        Complexity: O(n) time, O(1) space.
        """
        if len(s) != len(t):
            return False

        cnt = [0] * 26
        base = ord('a')

        for ch in s:
            cnt[ord(ch) - base] += 1
        for ch in t:
            i = ord(ch) - base
            cnt[i] -= 1
            if cnt[i] < 0:          # early fail
                return False
        return True
