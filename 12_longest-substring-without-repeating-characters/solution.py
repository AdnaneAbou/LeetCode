# This Solution is O(n^3). and submission not accepted because of time complexity ! 


def check_rep(s):
    """
    :stype s : string
    :rtype : boolean
    """
    return len(s) == len(set(s)) 


def max_length(substr):
    """
    :type max : List[str]
    :rtype max : int
    :rtype str: string
    """
    return max(len(s) for s in substr) if substr else 0
           

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    def check_rep(s):
        return len(s) == len(set(s)) 
    def max_length(substr):
        return max(len(s) for s in substr) if substr else 0
    substr = []
    n = len(s)
    for i in range(n):
        for j in range(i+  1 , n + 1):
            temp = s[i:j]
            if check_rep(temp):
                substr.append(temp)
    ma  = max_length(substr)

    return ma 


s = "au"


ma  = lengthOfLongestSubstring(s)
print( ma  )

