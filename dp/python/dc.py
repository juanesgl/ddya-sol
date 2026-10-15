from sys import stdin as sd 

def read(f):
    return f.readline().strip() 

def fr(d, i, memo, coins, m): 
    if i == m:
        return d  
    
    if (d, i) in memo: 
        return memo[(d, i)] 

    opcionA = fr(d + coins[i], i + 1, memo, coins, m)
    opcionB = fr(abs(d - coins[i]), i + 1, memo, coins, m)

    res = min(opcionA, opcionB)

    memo[(d, i)] = res 

    return res

def main(f):
 
    t = int(read(f))
    
    for _ in range(t):
        read(f)  
        coins = [int(i) for i in read(f).split()]
        
        memo = {}
        ans = fr(0, 0, memo, coins, len(coins))
        
        print(ans)

main(sd)