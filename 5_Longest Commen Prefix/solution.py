def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    common = ""
    return_common = ""
    i=0

    if len(strs) ==  1:
        common = strs[0]
    while True: 
        list_first_chars = []

        for str in strs:
            if i >=  len(str):
                return return_common
            

            val = str[i]
            list_first_chars.append(val)
        
        for iter in range(len(list_first_chars)-1):
            if (list_first_chars[0] != list_first_chars[iter+1]):
                return return_common
            common = list_first_chars[iter]

        return_common += common
        i+=1
        
        
common = longestCommonPrefix(["aadnan","aadnanv"])
print(common)
#  aadnan