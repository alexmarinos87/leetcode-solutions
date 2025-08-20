class Solution(object):
    def isValid(self, s):
        """
        Approach: Use a stack. Push opens; on a close, check top-of-stack.
        Complexity: O(n) time, O(n) space (worst case all opens).
        """
        if len(s) & 1:  # odd length can't be valid
            return False

        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:  # ch is a closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack

