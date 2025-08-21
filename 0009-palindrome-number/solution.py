class Solution(object):
    def isPalindrome(self, x):
        """
        Approach:
            - Negative numbers are not palindromes.
            - If x ends with 0 (and x != 0), it can't be a palindrome.
            - Reverse only the lower half of the digits:
                rev accumulates the reversed tail while x shrinks from the head.
                Stop when rev >= x (we've processed half the digits).
              Then:
                - Even digits: x == rev
                - Odd digits : x == rev // 10 (drop the middle digit)

        Why it fits:
            - Reversing only half avoids overflow concerns and keeps O(1) space.
            - Early eliminations (negative, trailing zero) prune impossible cases fast.

        Invariant:
            - At each loop step, rev is the reverse of the processed suffix,
              and the unprocessed prefix is in x. The original number equals
              concat(prefix=x, reverse(prefix or prefix without middle)=rev).

        Correctness:
            - For palindromes, left half equals reversed right half (ignoring middle).
              The loop stops exactly at the halfway point, making the final equality check decisive.

        Complexity:
            - Time: O(log₁₀ n) digit operations
            - Space: O(1)
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + (x % 10)
            x //= 10

        return x == rev or x == rev // 10

