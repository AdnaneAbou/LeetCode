def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    letters_map = {"2": ["a","b","c"] ,"3": ["d","e","f"] 
                ,"4":["g","h","i"] ,"5": ["j","k","l"]
                ,"6":["m","n","o"] ,"7":["p","q","r","s"]
                ,"8":["t","u","v"] ,"9": ["w","x","y","z"]}
    output = []

    def backtrack(current_combination, i):

        if len(digits) == 0:
            return []
        if len(current_combination) == len(digits):
            output.append(current_combination)
            return
        
        for c in letters_map[digits[i]]:
            backtrack(current_combination + c,i+1)   
    
    if digits:
        backtrack("",0)
    return output

print(letterCombinations(digits = ""))