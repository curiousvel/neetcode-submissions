class Solution:
    """
    🧠 MENTAL MODEL: The Unique Character Train (Variable Sliding Window)
    
    We want to find the longest stretch of a string without any repeating characters. 
    We use a Hash Set ('sett') to act as our passenger manifest—it tracks exactly 
    who is currently inside our window.
    
    1. EXPAND (Outer Loop): The 'right' pointer moves forward, inviting the next 
       character to board the train.
    2. CLEAN UP (Inner Loop): If the incoming character is ALREADY on the train 
       (a duplicate!), the 'while' loop kicks in. The 'left' pointer starts moving 
       forward, removing passengers from the front of the train one-by-one until 
       the duplicate character is booted off.
    3. RECORD: Once the train is verified to be 100% unique, we calculate its current 
       length ('right - left + 1') and update our historical 'longest' record.
    
    Complexity:
        - Time: O(N) -> Each character is added to the set once by 'right' and removed 
                       at most once by 'left'. Strictly linear time!
        - Space: O(min(N, M)) -> Where M is the size of the alphabet/charset. The set 
                                 will store unique characters up to the string length.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sett = set() # Use a set to store characters in the current window for O(1) lookup
        left = 0
        longest = 0

        # Iterate with the right pointer to expand the window
        for right in range(n):
            # If the character at 'right' is already in the set, shrink the window from the 'left'.
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            # Add the new character to the set
            sett.add(s[right])
            # Calculate the current length of the unique substring
            length = right - left + 1
            # Update 'longest' if the current window length is greater
            longest = max(length, longest)

        # Return the maximum length of the unique substring found
        return longest