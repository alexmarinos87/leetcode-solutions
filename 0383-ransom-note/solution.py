class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        Approach: Fixed-size frequency array for 26 lowercase letters.
                  Count magazine, then consume for ransomNote; early fail if any count goes negative.

        Complexity: Time O(n + m), Space O(1) (always 26 integers)
        """
        if len(ransomNote) > len(magazine):
            return False

        cnt = [0] * 26
        base = ord('a')
        for ch in magazine:
            cnt[ord(ch) - base] += 1

        for ch in ransomNote:
            i = ord(ch) - base
            cnt[i] -= 1
            if cnt[i] < 0:
                return False
        return True

