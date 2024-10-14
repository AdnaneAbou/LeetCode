
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict_values = {"I": 1, "V": 5, "X": 10, "L":50,"C":100,"D":500,"M":1000}
    res = 0
    i=0
    while i < len(s):
        

        if( i < len(s)-1 and ((s[i] == 'I' and s[i+1] == 'V') or( s[i] == 'I' and s[i+1] == 'X'))):
            res += dict_values[s[i+1]] - dict_values[s[i]] 
            i = i + 2
            continue
        
        elif(i < len(s)-1 and  ((s[i] == 'X' and s[i+1] == 'L' )or (s[i] == 'X' and s[i+1] == 'C'))):
            res += dict_values[s[i+1]] - dict_values[s[i]] 
            i = i + 2
            continue
        
        elif(i < len(s)-1 and  ((s[i] == 'C' and s[i+1] == 'D') or( s[i] == 'C' and s[i+1] == 'M' ))):
            res += dict_values[s[i+1]] - dict_values[s[i]] 
            i = i + 2
            continue
        

        res = res + dict_values[s[i]]
        i= i + 1

    return res


res = romanToInt(s)
print("resutl: " , res)
