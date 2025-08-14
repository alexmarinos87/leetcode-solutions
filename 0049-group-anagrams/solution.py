class Solution(object):
    def groupAnagrams(self, strs):
        """
        Group Anagrams (LeetCode 49)

        Approach
        --------
        Counting-signature hash (O(n * k)):
        - For each word, build a 26-length frequency vector (since inputs are lowercase a–z).
        - Use the frequency tuple as a dictionary key and append the word to that group.
        - This avoids per-word sorting (O(k log k)) and yields O(k) per word.

        Parameters
        ----------
        strs : List[str]
            List of lowercase strings to group.

        Returns
        -------
        List[List[str]]
            Groups of anagrams; order of groups and words within groups is arbitrary.
        """
        from collections import defaultdict

        groups = defaultdict(list)
        for w in strs:
            counts = [0] * 26
            for ch in w:
                counts[ord(ch) - ord('a')] += 1
            groups[tuple(counts)].append(w)

        return list(groups.values())

        # --- Alternative (simpler, slightly slower) ---
        # from collections import defaultdict
        # groups = defaultdict(list)
        # for w in strs:
        #     key = ''.join(sorted(w))
        #     groups[key].append(w)
        # return list(groups.values())

