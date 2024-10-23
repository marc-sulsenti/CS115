'''
Created on  October 20th 2022
@author:   Marc Sulsenti
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 4 
'''
l_memo={} # memo for fast_lucas
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    #Understand lucas nums as the a number, which is created by the sum of the last two behind it.
    if n in l_memo:  #memoization
        return l_memo[n]
    if (n <= 0): #Last number will be 2
        result = 2
    elif(n == 1):  # second to last number is 1
        result = 1 
    else:
        result = fast_lucas (n-1) + fast_lucas (n-2) #recursively returns the nth lucas number
        l_memo[n] = result
        return result
    return result

coin_memo = {} #empty memo dictionary for fast_change

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if(amount in coin_memo):
        return coin_memo[amount]
    elif (amount <=0 and coins ==[]):
        coin_memo[amount]=0
        return 0
    elif (coins == []):
        coin_memo[amount] = float("inf") #represents infinity
        return float("inf")
    elif(coins[0] > amount):
        return fast_change(amount,coins[1:]) #dont use index 0 if index 0 > amount
    else:
        use = 1+fast_change(amount-coins[0],coins) #use it
        lose=fast_change(amount,coins[1:]) # lose it
        ans = min(use,lose)
        coin_memo[amount]=ans
        return ans
        
      
    

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


