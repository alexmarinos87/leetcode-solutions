class Solution(object):
    def simplifyPath(self, path):
        """
        Approach: Split by '/' to get components. Skip '' and '.'.
                  For '..' pop one dir if possible; otherwise ignore.
                  Push any other name. Join with a single leading '/'.

        Complexity: O(n) time and O(n) space in worst case (n = len(path)).
        """
        stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)

