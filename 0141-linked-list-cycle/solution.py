# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

class Solution(object):
    def hasCycle(self, head):
        """
        Approach:
            Two pointers: slow (1 step), fast (2 steps). If they ever meet, a cycle exists.

        Why it fits:
            Detects cycles without extra memory and with a single pass.

        Invariant:
            After k iterations, slow has advanced k nodes and fast 2k nodes; within a cycle,
            their relative distance (mod cycle_length) decreases by 1 each step.

        Correctness:
            • Acyclic: fast hits None → return False.
            • Cyclic: relative motion ensures slow == fast eventually → return True.

        Complexity:
            Time O(n); Space O(1).
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

