def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    for i in range(len(haystack)):
        if haystack[i:len(needle)+i] == needle:
            return i
    
    return -1


res = strStr(haystack="sadbut" , needle ="sad")
print(res)