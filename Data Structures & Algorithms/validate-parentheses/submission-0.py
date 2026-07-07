class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Quick optimization check: Parentheses always come in pairs. 
        # If the string length is odd, it's impossible for all of them to match.
        if len(s) % 2 != 0:
            return False

        # 2. Initialize a deque to act as our Last-In, First-Out (LIFO) stack.
        stack = deque()
        
        # 3. Map closing brackets to their corresponding opening brackets.
        # This keeps our lookup clean and scalable.
        comparision_map = {')': '(', ']': '[', '}': '{'}

        for c in s:
            # 4. If the character is a CLOSING bracket
            if c in comparision_map:
                # - 'not stack': Safety check. If the stack is empty, there is no
                #   matching opening bracket for this closing bracket (e.g., s = "][")
                # - 'stack.pop() != ...': Pops the top of the stack and checks if it
                #   matches the expected opening bracket for the current character.
                if not stack or stack.pop() != comparision_map[c]:
                    return False    
            
            # 5. If the character is an OPENING bracket
            else:
                # Push it onto the stack to wait for its matching closing bracket.
                stack.append(c)

        # 6. Final verification: If the stack is completely empty, all brackets 
        # were matched and closed in the correct order. 
        # If any leftovers remain (e.g., s = "(("), it returns False.
        return len(stack) == 0