class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken = set(brokenLetters)
        count = 0
        for word in text.split():
            if broken.isdisjoint(word):
                count += 1
        return count

