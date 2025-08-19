class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        Approach: Greedy pack then distribute spaces.
        Why it fits: The spec requires greedy line breaks and left-biased, even space distribution.
        Invariants: For a line [i:j], total_chars + (j-i-1) <= maxwidth and adding words [j] would overflow.
        Correctness: For non-last lines, divmod(total_spaces, gaps) gives base q and remainder r; the first r gaps recieve q+1 spaces (left bias). Last line and single-word lines are left-justified.
        Complexity: Time O(total characters), Space O(1) extra beyond output.
        """
        res = []
        n = len(words)
        i = 0

        while i < n:
            # Greedily take as mmany words as fit in this line
            total = len(words[i]) # sum of word lengths in the line
            j = i + 1
            while j < n and total + len(words[j]) + (j - i) <= maxWidth:
                total += len(words[j])
                j += 1
            
            gaps = j - i - 1
            spaces = maxWidth - total
            last_line = (j == n)

            if last_line or gaps == 0:
                # Left-justify: single spaces between words, pad end
                line = ' '. join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                q, r = divmod(spaces, gaps) # r leftmost gaps get one extra
                parts = []
                for k in range(i, j - 1):
                    parts.append(words[k])
                    parts.append(' ' * (q + (1 if k - i < r else 0)))
                parts.append(words[j - 1])
                line = ''.join(parts)

            res.append(line)
            i = j
        
        return res
