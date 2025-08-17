class MinStack(object):
    def __init__(self):
        """
        Min Stack (LeetCode 155)

        Approach
        --------
        Store pairs (value, current_min) on a single stack.
        - On push: current_min = min(val, stack[-1].current_min) if stack else val
        - On pop/top/getMin: read from the top tuple.
        All ops are O(1).
        """
        self._stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur_min = val if not self._stack else (self._stack[-1][1] if self._stack[-1][1] < val else val)
        self._stack.append((val, cur_min))

    def pop(self):
        """
        :rtype: None
        """
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self._stack[-1][1]
