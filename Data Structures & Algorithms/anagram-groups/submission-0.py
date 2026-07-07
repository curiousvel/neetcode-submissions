class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 
        # Time complexity: O(m*n). Method: Frequency counting
        result_map = defaultdict(list)

        # List to create a key based on chars in str.
        for s in strs:
            key = [0] * 26 # a..z
            
            for c in s:
                key[ord(c) - ord('a')] += 1 # Find ascii value and add 1

            # add value to the key. Convert key to tuple as we need immutable key
            result_map[tuple(key)].append(s)

        return list(result_map.values())