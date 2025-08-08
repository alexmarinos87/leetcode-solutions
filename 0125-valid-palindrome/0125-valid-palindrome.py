class Solution(object):
    def isPalindrome(self, s):
        """
        Determine if the given string is a palindrome after:
        - Converting all letters to lowercase.
        - Removing all non-alphanumeric characters.

        Approach:
        - Use two pointers, one starting from the left and the other from the right.
        - Move each pointer inward, skipping non-alphanumeric characters.
        - Compare characters in lowercase; if any mismatch is found, return False immediately.
        - If the pointers cross without mismatches, return True.

        Parameters
        ----------
        s : str
            Input string, may contain letters, numbers, spaces, and punctuation.

        Returns
        -------
        bool
            True if the processed string is a palindrome, False otherwise.
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
