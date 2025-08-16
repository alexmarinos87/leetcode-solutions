class Solution(object):
    def isValid(self, s):
        """
        Valid Parentheses (LeetCode 20)

        Approach
        --------
        Stack matching (O(n)):
        - Push opening brackets onto a stack.
        - For each closing bracket, check it matches the top of the stack.
        - If mismatch or stack is empty, return False.
        - At the end, stack must be empty.

        Parameters
        ----------
        s : str
            String consisting only of '()[]{}'.

        Returns
        -------
        bool
            True if the parentheses are valid; False otherwise.
        """
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs.get(ch):
                    return False
                stack.pop()

        return not stack
