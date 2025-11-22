class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        # Use arrays of size 26 instead of a dictionary
        first = [len(s)] * 26
        last = [-1] * 26

        # Record first and last occurence of each characters
        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            first[index] = min(first[index], i)
            last[index] = max(first[index], i)

        ans = 0

        # For each possible outer character
        for index in range(26):
            l = first[index]
            r = last[index]
            if l < r: # Must have at least two occurences
                """
                This avoids:
                    - Python sets
                    - Uses integer operations (very fast)
                    - Uses a 26 bit integer to represent which middle characters exist
                """
                # Step by Step Bitmask Logic
                # Create a 26 bit integer 
                mask = 0
                # 00000000000000000000000000000  
                # 26 intenger all 0s
                # Each bit corresponds to a latter 'a' to 'z'
                for k in range (l + 1, r):
                    # When you encoutner a character y in the middle region
                    mask |= 1 << (ord(s[k]) - ord('a'))
                    # The bit is set to 1
                    # For example:
                    #   - 'b' |= 1 << 1 = 00010
                    #   - 'f' |= 1 << 5 = 1000000
                    # if middle characters were b, c, f then mask becomes:
                    # 000100000110
                ans += mask.bit_count()
                # We count the number of 1 bits using mask.bit_count

        return ans
