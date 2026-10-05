## progamación dinámica bottom-up
def calcularSk(k):
    if k<1:
        raise ValueError("k debe ser >= 1")
    if 1<=k<=2:
        return 1
    
    dp=dict()
    dp[1]=dp[2]=1
    
    for i in range(3,k+1):
        dp[i]=dp[i-1]+dp[i-2]
        
    return dp[k]
        

    
    