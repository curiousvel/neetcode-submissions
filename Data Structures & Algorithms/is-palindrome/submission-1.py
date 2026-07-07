class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not self.isalphanum(s[start]):
                start += 1
            while start < end and not self.isalphanum(s[end]):
                end -= 1
            
            if s[start].lower() != s[end].lower():
                return False
            
            start, end = start + 1, end -1

        return True

    def isalphanum(self, c):
        char = ord(c)
        return (char >= ord('A') and char <= ord('Z') or
            char >= ord('a') and char <= ord('z') or
            char >= ord('0') and char <= ord('9')
            )