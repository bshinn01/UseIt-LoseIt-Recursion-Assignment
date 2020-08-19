''' Name:Breanna Shinn

Date:09-26-19

CS115 - HW 2 ~ Recursion

Pledge: I pledge my honor that I have abided by the Stevens Honor System.

'''

## Part 1 ~ Change

def makeChange(val, coins):
    '''A function that takes a number value (val) and a list of numbers (coins)
and determines the lowest possible number of coins needed to reach the given value,
if possible, and also returns a list of the coins used to make the value.'''

    if val == 0:
        return [0, []]

    elif val < 0 or coins == []:
        return [float("inf"), [] ]

    else:
        loseIt = makeChange(val, coins[1:])
        useIt = makeChange(val - coins[0], coins)

    useIt = [useIt[0] +1, useIt[1] + [coins[0]]]
    return min(useIt, loseIt)



## Part 2 ~ Least Common Substrings

def LCS(a, b):
    '''return the longest common subsequence'''
    if not (a and b):
        return ''
    elif (a[0]==b[0]):
        return str(a[0]) + str(LCS(a[1:], b[1:]))
    else:
        if max(len(LCS(a[1:], b)), len(LCS(a, b[1:]))) == len(LCS(a, b[1:])):
            return str(LCS(a, b[1:]))
        else:
            return str(LCS(a[1:], b))
    

def PLCS(a, b):
    s2 = LCS(a , b)
    count = 0
    if LCS(a,b) == '':
        return [[-1],[-1]]
    def helper(s1, s2, count):
        if not (s1 and s2):
            return list([])+list([])
        elif (s1[0] == s2[0]):
            return [count] + list(helper(s1[1:], s2[1:], count + 1))
        else:
            return list(helper(s1[1:], s2, count + 1))
            
    return [helper(a, s2, count), helper(b, s2, count)]
    
