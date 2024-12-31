def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    n_str = str(n)
    visited = set()
    def recursive(n_str):
        
        if n_str in visited:
            return False
        
        sum =0
        for digit in n_str:
            sum += int(digit)*int(digit)

        if sum ==1 :
            return True
        
        visited.add(n_str)

        return recursive(str(sum))
    
    return recursive(n_str)

    

print(isHappy(1))