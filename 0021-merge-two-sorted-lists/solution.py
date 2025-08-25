# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Approach:
            - Maintain a 'tail' pointer starting at a dummy node.
            - Repeatedly take the smaller head node from l1/l2 and append to tail.
            - Finally append the remaining list.

        Why it fits:
            - Takes advantage of the already-sorted order; single linear pass with O(1) extra space.

        Invariant:
            - The list starting at 'dummy.next' is a sorted merge of all nodes taken so far.
            - 'tail' always points to its last node.

        Correctness:
            - At each step the smallest remaining head is chosen, preserving global sorted order.
            - Termination appends the remaining sorted suffix, keeping the result sorted.

        Complexity:
            - Time: O(n + m) — n=len(l1), m=len(l2).
            - Space: O(1) extra — reuses nodes.
        """
        dummy = tail = ListNode()
        a, b = list1, list2
        while a and b:
            if a.val <= b.val:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next

