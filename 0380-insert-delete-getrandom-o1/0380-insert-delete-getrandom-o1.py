import random

class RandomizedSet(object):

    def __init__(self):
        """
        Use a list for values and a hash map to track indices.
        Time: O(1) avg per operation
        """
        self.indices = {}  # value -> index in self.nums
        self.nums = []     # list of current values

    def insert(self, val):
        """
        Add val if not present.
        Returns True if inserted, False if it already exists.
        Time: O(1) average
        """
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)  # index where it'll be appended
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        Remove val if present.
        Returns True if removed, False if it didn't exist.
        Time: O(1) average
        """
        if val not in self.indices:
            return False

        idx = self.indices[val]     # where val sits in the list
        last = self.nums[-1]        # last element in the list

        # Move the last element to fill the gap at idx
        self.nums[idx] = last
        self.indices[last] = idx

        # Remove the last slot
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        """
        Return a random element.
        Time: O(1)
        """
        return random.choice(self.nums)
