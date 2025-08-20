class Solution(object):
    def findSubstring(self, s, words):
        """
        Approach: Let L = len(one word), M = len(words). Build 'need' counts for words.
                  For each offset r in [0..L-1], slide a window in steps of L over s:
                  add current word, and while overfull or invalid, pop from left by L.
                  When window size reaches M words with counts matching 'need', record start.
        Why it fits: All words have equal length → we can slide in fixed strides, maintaining a multiset.
        Invariants: window contains only complete words; 'have' maps counts in the current window;
                    valid when have == need and window spans exactly M words.
        Correctness: Each candidate alignment (by offset) is checked; overfull counts are corrected
                     by advancing left, ensuring every valid concatenation is found once.
        Complexity: Time O(|s| + M*L) ≈ O(|s|) per offset → O(L*|s|) overall; Space O(M).
        """
        if not s or not words:
            return []

        from collections import Counter
        L = len(words[0])
        M = len(words)
        total_len = L * M
        n = len(s)
        if n < total_len:
            return []

        need = Counter(words)
        ans = []

        for offset in range(L):
            left = offset
            have = Counter()
            count_words = 0

            for right in range(offset, n - L + 1, L):
                word = s[right:right + L]
                if word in need:
                    have[word] += 1
                    count_words += 1
                    # shrink if overfull
                    while have[word] > need[word]:
                        left_word = s[left:left + L]
                        have[left_word] -= 1
                        left += L
                        count_words -= 1
                    # check full window
                    if count_words == M:
                        ans.append(left)
                        left_word = s[left:left + L]
                        have[left_word] -= 1
                        left += L
                        count_words -= 1
                else:
                    # reset window
                    have.clear()
                    count_words = 0
                    left = right + L

        return ans
