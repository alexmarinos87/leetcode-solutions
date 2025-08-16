class Solution(object):
    def simplifyPath(self, path):
        """
        Simplify Path (LeetCode 71)

        Approach
        --------
        Stack-based normalization (O(n)):
        - Split by '/'.
        - Skip '' and '.'.
        - On '..', pop if stack not empty.
        - Otherwise, push the directory name (including sequences like '...' which are valid names).
        - Join with '/' and prefix with '/'.

        Parameters
        ----------
        path : str
            Absolute Unix-style path.

        Returns
        -------
        str
            Canonical simplified path.
        """
        parts = path.split('/')
        stack = []
        for p in parts:
            if p == '' or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)

