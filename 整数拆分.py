n = 10
dp = [0] * (n + 1)

for i in range(2, n + 1):
    for j in range(i):
        print(f"is :{i}轮,{dp[i]},{j * dp[i - j]},{j * (i - j)}")
        dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
print(dp[n])
