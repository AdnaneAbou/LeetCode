
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    str_list = s.split()
    return len(str_list[-1])


print(lengthOfLastWord("luffy is still joyboy"))