class Solution(object):
    def majorityElement(self, nums):
        """
        Find the majority element that appears more than n // 2 times.

        This uses the Boyer-Moore Voting Algorithm:
        - Keep a running count of a candidate.
        - If count drops to zero, switch to a new candidate.

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        int
            The majority element in the list.
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num  # reset to new candidate
            count += (1 if num == candidate else -1)

        return candidate

