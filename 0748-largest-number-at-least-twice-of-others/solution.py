class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_value = max(nums)
        max_index = nums.index(max_value)

        second_largest = max(x for x in nums if x != max_value)

        if max_value >= 2 * second_largest:
            return max_index
        return -1
        
