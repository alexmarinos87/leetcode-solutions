class Solution(object):
    def intToRoman(self, num):
        """
        Convert an integer to its Roman numeral representation.

        Strategy:
        - Use a list of value-symbol pairs, ordered from largest to smallest.
        - Greedily subtract the largest possible value, appending its symbol to the result, until the number is reduced to 0.

        Parameters
        ----------
        num : int
            Integer in the range [1, 3999].

        Returns
        -------
        str
            The Roman numeral representation of num.
        """
        val_syms = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = []
        for value, symbol in val_syms:
            count, num = divmod(num, value)
            result.append(symbol * count)
        return "".join(result)

