class Solution(object):
    def calculate(self, s):
        """
        Approach: Scan once keeping:
          - res: running result outside the current number
          - sign: current sign to apply to the next number
          - stack: sign multipliers from surrounding parentheses
        Rules:
          '+'  → commit number, sign = stack[-1]
          '-'  → commit number, sign = -stack[-1]
          '('  → push current sign (to affect inner terms)
          ')'  → commit number, pop sign
        Spaces are ignored.

        Time O(n), Space O(n) in worst case (nested parentheses).
        """
        res = 0
        sign = 1
        stack = [1]   # sign context; top multiplies the local sign
        num = 0

        for c in s:
            if '0' <= c <= '9':
                num = num * 10 + (ord(c) - 48)
            elif c == '+' or c == '-' or c == ')':
                # commit the number seen so far
                res += sign * num
                num = 0
                if c == '+':
                    sign = stack[-1]
                elif c == '-':
                    sign = -stack[-1]
                else:  # ')'
                    stack.pop()
            elif c == '(':
                stack.append(sign)
            # ignore spaces

        res += sign * num
        return res

