class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize graph nodes for all unique characters
        adj = {char: set() for word in words for char in word}

        # Step 2: Build directed edges from adjacent word comparisons
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Edge Case: Invalid prefix ordering (e.g., ["apple", "app"])
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])  # w1[j] comes before w2[j]
                    break

        # Step 3: 3-State DFS Cycle Detection using Hash Map
        # 1 = Visiting (in recursion stack), 2 = Visited (fully processed)
        visit = {}
        result = []

        def dfs(char: str) -> bool:
            if char in visit:
                if visit[char] == 1:
                    return False  # Cycle detected
                if visit[char] == 2:
                    return True   # Already verified safe

            visit[char] = 1  # Mark as Currently Visiting

            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False  # Cycle detected downstream

            visit[char] = 2      # Mark as Visited/Safe
            result.append(char)  # Post-order append
            return True

        # Run DFS for every unique character
        for char in adj:
            if not dfs(char):
                return ""  # Invalid order due to cycle

        # Step 4: Reverse post-order result for valid topological order
        return "".join(result[::-1])