def plusOne( digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = 0
    c = 1
    for i in range(len(digits)-1,-1,-1):
        num += digits[i] * c 
        c = c * 10   
    num = num + 1
    return_list = [0] * len(str(num))
    iter = 1

    for i in range(len(str(num))-1,-1,-1):
       return_list[i] = (num //iter)%10
       iter = iter * 10

    return return_list


digits = [1,2,3,9]
print(plusOne( digits))


