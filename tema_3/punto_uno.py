## bottom-up
def calcularSk(k):
    if k<1:
        raise ValueError('K debe ser mayor o igual a 1.')
    if 1<=k<=3:
        return 1
    else:
        dp=dict()
        dp[1]=dp[2]=dp[3]=1
        
        for i in range(4, k+1):
            dp[i]=2*dp[i-1]+3*dp[i-2]+4*dp[i-3]
        
        return dp[k]

## topdown con memo
def calcularSkTopDown(k, memo=None):
    if k<1:
        raise ValueError('K debe ser mayor o igual a 1.')
    
    if memo is None:
        memo={}
    
    if k in memo:
        return memo[k]
    
    if 1<= k <=3:
        memo[k]=1
    
    else:
        memo[k]=(2*calcularSkTopDown(k-1, memo)+ 3*calcularSkTopDown(k-2, memo)+ 4*calcularSkTopDown(k-3, memo))
        
    return memo[k]
    
