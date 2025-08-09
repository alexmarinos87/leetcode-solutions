class Solution(object):
    def twoSum(self, numbers, target):
        """
        Find two numbers in a sorted array that sum to the target.

        Approach:
        - Use two pointers: one starting at the leftmost element, one at the rightmost.
        - Calculate the sum of the elements at the two pointers.
        - If the sum matches the target, return their indices (1-based).
        - If the sum is less than the target, move the left pointer rightwards to increase the sum.
        - If the sum is greater than the target, move the right pointer leftwards to decrease the sum.
        - This method ensures O(n) time complexity with O(1) extra space.

        Parameters
        ----------
        numbers : List[int]
            A sorted (non-decreasing) list of integers.
        target : int
            The sum to be achieved.

        Returns
        -------
        List[int]
            A list containing the 1-based indices [index1, index2] of the two numbers.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # convert to 1-based index
            elif current_sum < target:
                left += 1
            else:
                right -= 1

