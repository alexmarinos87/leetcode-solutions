class RandomizedSet(object):

    def __init__(self):
        """
        Use a list for values and a hash map to track indices.
        Time: O(1) avg per operation
        """
        self.indices = {}
        self.nums = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        Add val if not present.
        Time: O(1)
        """
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        Remove val if present
        Time: O(1)
        """
        if val not in self.indices:
            return False
        idx = self.indices[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.indices [last] = idx
        self.nums.pop()
        del self.indices[val]
        return True
        

    def getRandom(self):
        """
        :rtype: int
        Return a random element.
        Time: O(1)
        """
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()