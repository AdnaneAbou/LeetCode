class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}
        max_length = 0
        start = 0  # Start index of the current substring
        
        for end in range(len(s)):
            if s[end] in char_index_map:
                # Move the start pointer to the right of the last occurrence
                start = max(start, char_index_map[s[end]] + 1)
            
            # Update the last index of the character
            char_index_map[s[end]] = end
            
            # Calculate the length of the current substring
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example usage
sol = Solution()
print(sol.lengthOfLongestSubstring(""))  # Output: 3

# s ='ggggg'

# print(len(s)) 