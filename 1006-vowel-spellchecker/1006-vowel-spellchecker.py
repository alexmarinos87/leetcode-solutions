class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowels = set('aeiou')

        def devowel(s):
            # Replace vowels with '*', lowercase first
            s = s.lower()
            return ''.join('*' if ch in vowels else ch for ch in s)

        # 1) Exact matches (case-sensitive)
        exact = set(wordlist)

        # 2) Case-insensitive first occurrence map
        case_map = {}
        # 3) Devoweled (vowel-error) first occurrence map
        devowel_map = {}

        for w in wordlist:
            lw = w.lower()
            dv = devowel(w)
            # only set first occurrence
            if lw not in case_map:
                case_map[lw] = w
            if dv not in devowel_map:
                devowel_map[dv] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue

            lq = q.lower()
            if lq in case_map:
                ans.append(case_map[lq])
                continue

            dq = devowel(q)
            if dq in devowel_map:
                ans.append(devowel_map[dq])
            else:
                ans.append("")

        return ans
