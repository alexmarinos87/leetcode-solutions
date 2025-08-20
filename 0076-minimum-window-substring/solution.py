class Solution(object):
    def minWindow(self, s, t):
        """
        Approach: Expand right adding counts; when all required chars are covered (formed == need),
                  shrink left to minimize, updating best answer.
        Why it fits: We maintain the smallest valid window under “cover multiset of t” constraint.
        Invariants: have[c] >= need[c] for all c in t inside a valid window; formed counts how many
                    characters reach their required frequency.
        Correctness: Each time the window becomes valid we shrink to minimal, so the minimal valid
                     window over all positions is recorded.
        Complexity: Time O(|s| + |t|), Space O(Σ) for frequency maps.
        """
        from collections import Counter

        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        left = 0
        best_len = float('inf')
        best_start = 0

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                # update best
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                # shrink
                lc = s[left]
                have[lc] -= 1
                if lc in need and have[lc] < need[lc]:
                    formed -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]

