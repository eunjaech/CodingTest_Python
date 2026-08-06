def rob_linear(money):
    if len(money) == 1:
        return money[0]
    
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    
    return dp[len(money)-1]
def solution(money):
    if len(money) == 1:
        return money[0]
    
    case1 = rob_linear(money[:-1])  # 마지막 집 제외
    case2 = rob_linear(money[1:])   # 첫 집 제외
    
    return max(case1, case2)