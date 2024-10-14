



def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    a = 1
    carry = (x//a) % 10
    numbers = []
    val = False
    while (((x//a) > 0 and x > 0 ) or( x==0 and a==1 )):
        numbers.append(carry)
        a = a*10
        carry = (x//a) % 10
       
    print(numbers)
    for i in range(len(numbers)):

        if(numbers[i] != numbers[-(i+1)]):
            print(numbers[i] ,"  ",numbers[-i-1]," i = ",i)
            val = False
            break
        else: 
            val = True
        
    
    return val
    

bool_ = isPalindrome(1000021)
print(bool_)

# print(-159//10)