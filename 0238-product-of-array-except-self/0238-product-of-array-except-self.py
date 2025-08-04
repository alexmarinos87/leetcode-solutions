class Solution(object):
    def productExceptSelf(self, nums):
        """
        For each index i, compute the product of all elements in the array except nums[i],
        without using division, in O(n) time and O(1) extra space (output array excluded).

        Strategy:
        - First pass: compute prefix products and store in result.
        - Second pass: multiply suffix products into result.

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        List[int]
            Output list where result[i] = product of all nums[j] where j != i
        """
        n = len(nums)
        result = [1] * n

        # Step 1: Compute prefix products (product of all elements to the left)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: Multiply by suffix products (product of all elements to the right)
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
