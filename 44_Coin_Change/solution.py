def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    dp = [amount +1 ] * (amount +1 ) # amount : min coin ( = min(amount // coin[i]))
    dp[0] = 0 
    
    for i in range(1,amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i] , 1 + dp[i - coin]) 

    return dp[amount] if dp[amount] != amount +1 else -1

coins = [1,2,5]
amount = 5

print(coinChange(coins,amount))