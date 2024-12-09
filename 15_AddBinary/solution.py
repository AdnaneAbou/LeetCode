def addBinary( a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    i , j = len(a) -1 , len(b) -1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >=0 :
            total += int(a[i])
            i -= 1
        if j >= 0 :
            total += int(b[j])
            j -= 1
        carry = total // 2
        result.append(str(total % 2))
    
    return ''.join(result[::-1])




    


print(addBinary(a='0',b='0'))
