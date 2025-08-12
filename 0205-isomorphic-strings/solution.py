class Solution(object):
    def isIsomorphic(self, s, t):
        """
        Isomorphic Strings (LeetCode 205)

        Approach
        --------
        Enforce a bijection using two hash maps (O(n)):
        - Map chars from s -> t and t -> s simultaneously.
        - On each pair (a, b), if an existing mapping conflicts, return False.
        - If we finish without conflicts, the mapping is one-to-one and onto.

        Parameters
        ----------
        s : str
            Source string.
        t : str
            Target string of the same length.

        Returns
        -------
        bool
            True if s and t are isomorphic; False otherwise.
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

        # --- Alternative (pattern encoding) ---
        # def pattern(x):
        #     seen, out = {}, []
        #     for i, ch in enumerate(x):
#             seen.setdefault(ch, len(seen))
        #         out.append(seen[ch])
        #     return tuple(out)
        # return pattern(s) == pattern(t)

