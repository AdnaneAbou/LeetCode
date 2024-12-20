def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    res = ""
    resLength = 0 

    for i in range(len(s)):
        # Check for odd-length palindromes (center at i)
        left , right = i ,i 
        while left >=0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1 ) > resLength : 
                res = s[left:right+1]
                resLength = right - left + 1
            left -= 1 
            right += 1
            
        left , right = i ,i + 1
        while left >=0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1 ) > resLength : 
                res = s[left:right+1]
                resLength = right - left + 1
            left -= 1 
            right += 1

    return res
            
print(longestPalindrome("adnbbsadngjgnda"))


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromes = {} 

        for i in range(len(s)):
            length = 1  
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length += 2
                left -= 1
                right += 1
            palindromes[i] = length

            length = 0
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length += 2
                left -= 1
                right += 1
            if length > 0: 
                palindromes[i] = max(palindromes.get(i, 0), length)

        center = max(palindromes, key=palindromes.get)
        max_length = palindromes[center]

        if max_length % 2 == 0:
            start = center - (max_length // 2) + 1
        else:
            start = center - (max_length // 2)
            
        end = center + (max_length // 2) + 1

        # Extract the longest palindrome substring
        longest_palindrome = s[start:end]
        return longest_palindrome
    

sol = Solution()
print(sol.longestPalindrome("cbb"))
