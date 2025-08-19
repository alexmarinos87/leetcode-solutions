class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        Approach: Left-to-right scan with lookahead.
        Map each symbol to a value. For positioni, if value(s[i]) < value(s[i+1]), subtract it; otherwise add it. This directly captures subtractive pairs. 
        Correctness: Each subtractive pair (e.g., 'IV' where 1 < 5) contributes -1 + 5 = 4; otherwise symbols add normally. Every index is processed exactly once.
        Complexity: Time O(n), Space O(1)
        """
        val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        total = 0
        n = len(s)
        for i in range(n):
            v = val[s[i]]
            if i + 1 < n and v < val[s[i+1]]:
                total -= v
            else:
                total += v
        return total