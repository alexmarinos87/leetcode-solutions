class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        # Collect numbers by remainder
        rem1 = []
        rem2 = []
        for x in nums:
            r = x % 3
            if r == 1:
                rem1.append(x)
            if r == 2:
                rem2.append(x)

        if total % 3 == 0:
            return total

        # Sort so we can pick smallest ones
        rem1.sort()
        rem2.sort()

        INF = 10**18 # big number as impossible placeholder

        if total % 3 == 1:
            # Option A remove one smallest remainder-1 number
            remove_one = rem1[0] if len(rem1) >= 1 else INF

            # Option B remove two smallest remainder-2 numbers
            remove_two = rem2[0] + rem2[1] if len(rem2) >= 2  else INF

            return total - min(remove_one, remove_two)

        else: # Total % 3 == 2:
            # Option A remove one smallest remainder-1 number
            remove_one = rem2[0] if len(rem2) >= 1 else INF

            # Option B remove two smallest remainder-2 numbers
            remove_two = rem1[0] + rem1[1] if len(rem1) >= 2 else INF

            return total - min(remove_one, remove_two)

