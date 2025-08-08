class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        Fully justify text to exactly maxWidth characters per line.

        Strategy:
        - Greedily pack words into each line without exceeding maxWidth.
        - For each non-final line with multiple words, distribute spaces as evenly as possible:
          * base spaces per gap = total_spaces // gaps
          * the leftmost (total_spaces % gaps) gaps get one extra space.
        - For the final line, or any line with a single word, left-justify and pad the end.

        Parameters
        ----------
        words : List[str]
            Input words (non-empty, no spaces within a word).
        maxWidth : int
            Target line width.

        Returns
        -------
        List[str]
            Fully justified lines, each of length exactly maxWidth.
        """
        res = []
        n = len(words)
        i = 0

        while i < n:
            # 1) Greedily select words for the current line
            j = i
            line_len = 0  # total chars of words only (no spaces yet)
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            # words[i:j] go on this line
            num_words = j - i
            gaps = num_words - 1
            is_last_line = (j == n)

            if is_last_line or gaps == 0:
                # 2) Left-justify: single spaces between words, pad the end
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                # 3) Fully justify: distribute spaces across gaps (left gets more when uneven)
                total_spaces = maxWidth - line_len
                base = total_spaces // gaps
                extra = total_spaces % gaps

                line_parts = []
                for k in range(gaps):
                    line_parts.append(words[i + k])
                    # Leftmost 'extra' gaps receive one additional space
                    spaces = base + (1 if k < extra else 0)
                    line_parts.append(" " * spaces)
                line_parts.append(words[j - 1])  # last word (no trailing spaces after)
                line = "".join(line_parts)

            res.append(line)
            i = j

        return res

