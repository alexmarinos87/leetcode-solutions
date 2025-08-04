import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize the data structure.
        - self.nums: list to store values
        - self.pos: dict to store value -> index mapping
        """
        self.nums = []
        self.pos = {}

    def insert(self, val):
        """
        Insert val if not present. Return True if inserted, False if already exists.
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        Remove val if present. Return True if removed, False if not found.
        """
        if val not in self.pos:
            return False
        
        # Get index of the element to remove
        idx = self.pos[val]
        last_element = self.nums[-1]

        # Swap the last element into the position of the element to remove
        self.nums[idx] = last_element
        self.pos[last_element] = idx

        # Remove the last element
        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        """
        Return a random element from the set.
        """
        return random.choice(self.nums)

