class Solution(object):
    def isIsomorphic(self, s, t):
        """
        Approach: Maintain two maps s->t and t->s to enforce a bijection.
        Complexity: O(n) time, O(min(n, Σ)) space (Σ ≤ 256 for ASCII).
        """
        if len(s) != len(t):
            return False

        st, ts = {}, {}
        for a, b in zip(s, t):
            if (a in st and st[a] != b) or (b in ts and ts[b] != a):
                return False
            st[a] = b
            ts[b] = a
        return True

