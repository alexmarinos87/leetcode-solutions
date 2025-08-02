class Solution(object):
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps in-place using reversal.

        Steps:
        1. Reverse the whole array.
        2. Reverse the first k elements.
        3. Reverse the rest.

        This achieves the rotation without using extra space.

        Parameters
        ----------
        nums : List[int]
        k : int

        Returns
        -------
        None
            The list `nums` is modified in-place.
        """
        n = len(nums)
        k %= n  # In case k is larger than the array length

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)      # Reverse entire array
        reverse(0, k - 1)      # Reverse first k elements
        reverse(k, n - 1)      # Reverse the rest

