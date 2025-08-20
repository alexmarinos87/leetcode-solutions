class Solution(object):
    def evalRPN(self, tokens):
        """
        Approach: Scan left→right. Push numbers to a stack.
                  On operator, pop b then a, compute a (op) b, push result.
                  Division must truncate toward zero.

        Complexity: O(n) time, O(n) space (stack).
        """
        def tdiv(a, b):
            # integer division truncated toward zero
            return (abs(a) // abs(b)) * (1 if a * b >= 0 else -1)

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': tdiv,
        }

        st = []
        for tok in tokens:
            if tok in ops:
                b = st.pop()
                a = st.pop()
                st.append(ops[tok](a, b))
            else:
                st.append(int(tok))
        return st[-1]

