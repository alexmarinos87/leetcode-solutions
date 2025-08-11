class Solution(object):
    def findSubstring(self, s, words):
        """
        Substring with Concatenation of All Words (LeetCode 30)

        Approach
        --------
        Fixed-size sliding windows by word offset (O(n)):
        - Let L be the common word length and M be len(words); each valid window has total length T = L*M.
        - Build a frequency map `need` of the words.
        - For each start offset in [0..L-1], slide a window in steps of L:
          * Add the next L-length chunk; if it’s not in `need`, reset the window.
          * If a word count exceeds `need`, shrink from the left by one word at a time.
          * When the window holds exactly M words with valid counts, record the left index,
            then slide by removing one word from the left to keep searching overlaps.
        - Works efficiently because we never revisit characters except via L disjoint passes.

        Parameters
        ----------
        s : str
            The input string to search within.
        words : List[str]
            List of words (all the same length).

        Returns
        -------
        List[int]
            Starting indices of all substrings that are a concatenation of every word exactly once,
            in any order. May be returned in any order.
        """
        if not s or not words:
            return []
        L = len(words[0])
        if L == 0:
            return []  # undefined/degenerate; avoid infinite loops
        M = len(words)
        T = L * M
        if len(s) < T:
            return []

        from collections import Counter, defaultdict
        need = Counter(words)
        res = []

        for offset in range(L):
            left = offset
            count = 0
            window = defaultdict(int)

            # step through s by word length
            for right in range(offset, len(s) - L + 1, L):
                w = s[right:right + L]
                if w in need:
                    window[w] += 1
                    count += 1

                    # shrink if this word is overrepresented
                    while window[w] > need[w]:
                        wl = s[left:left + L]
                        window[wl] -= 1
                        left += L
                        count -= 1

                    # full window found
                    if count == M:
                        res.append(left)
                        wl = s[left:left + L]
                        window[wl] -= 1
                        left += L
                        count -= 1
                else:
                    # reset window
                    window.clear()
                    count = 0
                    left = right + L

        return res
