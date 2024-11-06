thing_num = 4
all_capa = 5
volume_ = [1, 2, 3, 4]
value_ = [2, 4, 4, 5]

# 一维数组实现
dp = [0 for _ in range(all_capa + 1)]

for i in range(thing_num):
    for j in range(all_capa, volume_[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - volume_[i]] + value_[i])
print(max(dp))

