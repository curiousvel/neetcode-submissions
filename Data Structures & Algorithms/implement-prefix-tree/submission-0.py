class TrieNode:
    """
    Represents a single node in the Trie structure.
    
    Attributes:
        children (dict): Maps characters to their corresponding TrieNode children.
                         Example: {'a': TrieNode(), 'b': TrieNode()}
        is_end_of_word (bool): Flag indicating if this node represents the complete 
                                end of a word (rather than just a prefix).
    """
    def __init__(self):
        # A dictionary allows dynamic character storage, accommodating any character set
        # (ASCII, Unicode, uppercase/lowercase) without wasting unused array space.
        self.children = {}
        self.is_end_of_word = False


class PrefixTree:
    """
    Prefix Tree implementation supporting O(L) insert, exact search, and prefix search operations,
    where L is the length of the target string.
    """
    def __init__(self):
        # Initialize the root node. The root itself represents an empty string ""
        # and acts as the entry point for all words.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        
        Time Complexity: O(L) where L is the length of the word.
        Space Complexity: O(L) worst-case when inserting entirely new branch nodes.
        """
        # Start at the root of the tree
        node = self.root
        
        # Traverse through each character in the input string
        for char in word:
            # If the character does not exist in the current node's children map,
            # create a new child node to form a new branch path.
            if char not in node.children:
                node.children[char] = TrieNode()
            
            # Advance the pointer down to the child node corresponding to 'char'
            node = node.children[char]
            
        # Once the loop finishes, we are at the node representing the final character.
        # Mark this node as the end of a valid word.
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for an EXACT word match in the Trie.
        
        Time Complexity: O(L) where L is the length of the word.
        Space Complexity: O(1) auxiliary space.
        
        Returns:
            True if the exact word exists, False otherwise.
        """
        node = self.root
        
        # Traverse character by character
        for char in word:
            # If a character is missing, the word path was never inserted
            if char not in node.children:
                return False
            
            # Step into the matching child node
            node = node.children[char]
            
        # After traversing all characters, ensure the final node is marked as a 
        # completed word (e.g., searching for "app" when only "apple" was inserted returns False).
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that begins with the given prefix.
        
        Time Complexity: O(L) where L is the length of the prefix.
        Space Complexity: O(1) auxiliary space.
        
        Returns:
            True if any inserted word shares this prefix, False otherwise.
        """
        node = self.root
        
        # Traverse character by character along the prefix path
        for char in prefix:
            # If any character path is missing, no word starts with this prefix
            if char not in node.children:
                return False
            
            # Step into the matching child node
            node = node.children[char]
            
        # If we successfully traversed every character in the prefix without failing,
        # at least one word extends through or terminates at this point.
        return True