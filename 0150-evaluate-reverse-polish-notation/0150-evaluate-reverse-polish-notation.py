class Solution(object):
    def evalRPN(self, tokens):
        """
        Evaluate Reverse Polish Notation (LeetCode 150)

        Approach
        --------
        Stack evaluation (O(n)):
        - Scan tokens left→right.
        - Push numbers onto a stack.
        - On operator, pop right operand `b` then left operand `a`,
          compute a (op) b, and push the result.
        - Division must truncate toward zero (not floor). To make this
          Python 2/3 compatible, do sign-aware integer division:
              q = abs(a) // abs(b)
              result = q if a*b >= 0 else -q

        Parameters
        ----------
        tokens : List[str]
            RPN expression with integers and operators '+', '-', '*', '/'.

        Returns
        -------
        int
            The evaluated result (fits in 32-bit per constraints).
        """
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # '/'
                    # Truncate toward zero, Python-version agnostic
                    q = abs(a) // abs(b)
                    stack.append(q if a * b >= 0 else -q)
            else:
                stack.append(int(t))

        return stack[-1]
