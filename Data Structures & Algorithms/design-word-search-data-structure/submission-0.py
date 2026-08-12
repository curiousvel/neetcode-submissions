"""
LeetCode 211: Design Add and Search Words Data Structure

This module implements a Trie (Prefix Tree) with support for exact word insertion,
exact word matching, and wildcard search using '.' to match any single character.

Complexity Analysis:
- addWord:
    - Time:  O(L), where L is the length of the word being inserted.
    - Space: O(L) worst-case when creating new nodes for missing characters.
- search:
    - Time:  O(L) for exact string matching (no wildcards).
             O(N * 26^L) worst-case for wildcard searches, where N is total nodes
             and L is word length, as '.' forces branching across all child paths.
    - Space: O(L) recursion call-stack depth during DFS traversal.
"""


class TrieNode:
    """
    Represents an individual node within the Trie structure.
    
    Attributes:
        children (dict): Maps a character (str) to its corresponding child TrieNode.
                         Example: {'a': TrieNode(), 'b': TrieNode()}
        end_of_word (bool): Flag set to True if a valid inserted word terminates at this node.
    """
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    """
    Data structure supporting dynamic word addition and flexible search with wildcard matching.
    """

    def __init__(self):
        """Initializes the WordDictionary with an empty root node."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Inserts a word into the data structure.
        
        Args:
            word (str): The word string to store.
        """
        node = self.root

        # Traverse through each character in the input string
        for char in word:
            # Create a new TrieNode branch if the character path doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode()
            # Advance pointer down the tree
            node = node.children[char]

        # Mark the final node as a completed word boundary
        node.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the data structure.
        The input 'word' may contain dots '.' where '.' can match any single letter.
        
        Args:
            word (str): The word or pattern string to search.
            
        Returns:
            bool: True if a matching word exists, False otherwise.
        """

        def dfs(start: int, node: TrieNode) -> bool:
            """
            Performs a Depth-First Search traversal starting from index 'start' in 'word'
            using the target 'node' as the subtree root.
            """
            curr = node

            for i in range(start, len(word)):
                char = word[i]

                # --- Case 1: Wildcard Character '.' ---
                if char == '.':
                    # Branch out to EVERY child node at the current level
                    for child in curr.children.values():
                        # Advance index to 'i + 1' to process remaining characters
                        if dfs(i + 1, child):
                            return True  # Match found down this branch!
                    # If no child branch returns True, this wildcard path fails
                    return False

                # --- Case 2: Exact Character Match ---
                if char not in curr.children:
                    return False  # Path broken; character does not exist in children map
                
                # Advance pointer to the matching child node
                curr = curr.children[char]

            # After reaching the end of the word pattern, verify if this node completes a valid word
            return curr.end_of_word

        # Begin DFS from character index 0 starting at the root node
        return dfs(0, self.root)


# Example Usage:
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad")) # False
# print(obj.search("bad")) # True
# print(obj.search(".ad")) # True
# print(obj.search("b..")) # True