class Solution(object):
    def romanToInt(self, s):
        """
        Convert a Roman numeral string to its integer value.

        Strategy:
        - Use a dictionary to map Roman symbols to their values.
        - Traverse the string from left to right.
        - If a symbol is smaller than the one after it, subtract its value; otherwise, add it.

        Parameters
        ----------
        s : str
            Roman numeral string (guaranteed valid and in [1, 3999]).

        Returns
        -------
        int
            Integer value corresponding to the Roman numeral.
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)

        for i in range(n):
            value = roman_map[s[i]]
            # If the next symbol is larger, subtract current value (subtractive notation)
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= value
            else:
                total += value

        return total

