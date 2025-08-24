# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Approach:
            - Walk both lists in lockstep while a carry exists.
            - Sum current digits + carry, make a node with sum % 10, carry = sum // 10.
            - Use a dummy head so we can append in O(1).

        Why it fits:
            - Numbers are in reverse order, so addition proceeds naturally from head to tail.
            - Dummy head keeps code simple and avoids edge cases for the first node.

        Invariant:
            - After processing i nodes, the partial result encodes the sum of the first i digit-pairs
              (plus any earlier carry), and 'carry' equals the carry-out for the next position.

        Correctness:
            - Elementary column addition with carry ensures each output digit is correct.
            - Loop runs until both inputs are exhausted and carry is zero, so all digits are handled.

        Complexity:
            - Time: O(n + m) where n, m are lengths of l1, l2.
            - Space: O(n + m) for the new list (O(1) auxiliary).
        """
        dummy = tail = ListNode(0)
        carry = 0
        p, q = l1, l2
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            s = x + y + carry
            carry, digit = divmod(s, 10)
            tail.next = ListNode(digit)
            tail = tail.next
            p = p.next if p else None
            q = q.next if q else None
        return dummy.next

