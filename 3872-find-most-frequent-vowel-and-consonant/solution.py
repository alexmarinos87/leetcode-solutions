class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = set('aeiou')
        freq_vowels = {}
        freq_consonant = {}
        
        for char in s:
            if char in vowels:
                freq_vowels[char] = freq_vowels.get(char,0) + 1
            else:
                freq_consonant[char] = freq_consonant.get(char,0) +1

        max_freq_vowels = max(freq_vowels.values()) if freq_vowels else 0
        max_freq_consonant = max(freq_consonant.values()) if freq_consonant else 0

        return max_freq_vowels + max_freq_consonant
