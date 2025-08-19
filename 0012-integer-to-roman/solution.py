class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        Approach: Greedy by descending value-symbol pairs (incl. subtractives).
        Why it fits: Roman numerals are the concatenation of the largest representable tokens from {M, CM, D, CD, C, L, XL, X, IX, V, IV, I}. Repeatedly peel the largest token.
        Correctness: At each step choose the maximal value v <= num and append its symbol; subtract v and continue. Subtractive tokens ensure canonical form (no 4 in-a-row).
        Complexity: Time O(1) (fixed 13 tokens), Space O(1)
        """
        pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res = []
        for val, sym in pairs:
            if num == 0:
                break
            q, num = divmod(num, val)
            if q: 
                res.append(sym * q)
        return ''.join(res)
