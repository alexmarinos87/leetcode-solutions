class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Approach:
            - Treat each word as a node in a graph.
            - An edge exists between two words if they differ by exactly one character.
            - Use BFS to find the shortest path from beginWord to endWord.
            - Preprocess the word list into a mapping of wildcard patterns like h*t, ho*, etc. to reduce neighbor lookup time.

        Why it fits:
            - Minimum transformations in unweighted graph → BFS guarantees the shortest path.
            - Generic wildcard mapping efficiently finds neighboring words.

        Invariant:
            - Each BFS level corresponds to one transformation.
            - All intermediate transformations must exist in wordList.

        Correctness:
            - The BFS terminates on the first discovery of endWord, giving the minimum sequence length.

        Complexity:
            - Time: O(N * M^2), where N = len(wordList), M = length of each word (max 10)
            - Space: O(N * M) for the graph + visited set
        """
        from collections import defaultdict, deque

        if endWord not in wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                all_combo_dict[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            current_word, level = q.popleft()
            for i in range(L):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                for neighbor in all_combo_dict[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, level + 1))
                # Optional: clear the pattern to prevent revisiting
                all_combo_dict[pattern] = []
        return 0

