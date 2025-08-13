class Solution(object):
    def wordPattern(self, pattern, s):
        """
        Word Pattern (LeetCode 290)

        Approach
        --------
        Bijection check with two hash maps (O(n)):
        - Split s into words; if counts differ from len(pattern), return False.
        - Maintain maps char->word and word->char.
        - On each pair, ensure both mappings are consistent; otherwise return False.

        Parameters
        ----------
        pattern : str
            Pattern of lowercase letters.
        s : str
            Space-separated words.

        Returns
        -------
        bool
            True if there is a one-to-one mapping between letters in `pattern`
            and words in `s`; False otherwise.
        """
        words = s.split()
        if len(words) != len(pattern):
            return False

        p2w, w2p = {}, {}
        for ch, w in zip(pattern, words):
            if ch in p2w and p2w[ch] != w:
                return False
            if w in w2p and w2p[w] != ch:
                return False
            p2w[ch] = w
            w2p[w] = ch

        return True
