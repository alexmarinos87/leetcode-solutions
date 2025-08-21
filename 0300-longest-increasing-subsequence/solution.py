from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Approach:
            - Maintain an array `tails`, where tails[k] is the smallest possible tail
              of any increasing subsequence of length k+1 seen so far.
            - For each x in nums:
                * Find i = lower_bound(tails, x) (bisect_left).
                * If i == len(tails): append x (we extended the LIS).
                * Else: tails[i] = x (we improved a tail for length i+1).
        Why it fits:
            - The tails array stays sorted and compactly encodes all best tails;
              binary search makes updates O(log n).
        Invariant:
            - After processing each element, for every ℓ, there exists an increasing
              subsequence of length ℓ+1 ending at tails[ℓ], and tails is strictly increasing.
        Correctness:
            - Replacing tails[i] with a smaller x never reduces the ability to build
              longer subsequences; when we append, we've found a longer LIS.
              Thus len(tails) equals the LIS length.
        Complexity:
            - Time: O(n log n)
            - Space: O(n) for tails
        """
        tails = []
        for x in nums:
            i = bisect_left(tails, x)   # strict increase ⇒ lower_bound
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)

