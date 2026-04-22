def solution(n):    
    MOD = 1000000007
    
    # 홀수는 불가능
    if n % 2 == 1:
        return 0
    
    dp = [0] * (n + 1)
    
    dp[0] = 1
    dp[2] = 3
    
    # dp[n] += 2 * (dp[n-4] + dp[n-6] + ... + dp[0])
    # dp[n] = 3 * dp[n−2] + 2* (dp[n−4] + dp[n−6] + ... + dp[0])
    
    # dp[n] - dp[n-2] = (3dp[n-2] + 2(dp[n-4] + dp[n-6] + ... + dp[0]))
    #                 - (3dp[n-4] + 2(dp[n-6] + ... + dp[0]))
    #                 = = 3dp[n-2] + 2dp[n-4] - 3dp[n-4] = 3dp[n-2] - dp[n-4]
    # dp[n] = 4 * dp[n−2] − dp[n−4]
    
    for i in range(4, n + 1, 2):
        dp[i] = (4 * dp[i - 2] - dp[i - 4]) % MOD # 문제 조건
    
    return dp[n]