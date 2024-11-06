thing_num = 4
all_capa = 5
volume_ = [1, 2, 3, 4]
value_ = [2, 4, 4, 5]

dp = [[0 for _ in range(all_capa + 1)] for _ in range(thing_num)]

'''
  0 1 2 3 4 5
0 0 2 2 2 2 2
1
2
3
'''
# 初始化背包容量
for i in range(6):
    value = value_[0]
    capacity = volume_[0]
    if i < capacity:
        dp[0][i] = 0
    else:
        dp[0][i] = value
# 初始化背包
for i in range(4):
    dp[i][0] = 0

for i in range(1, thing_num):
    for j in range(1, all_capa + 1):
        no_i = dp[i - 1][j]
        add_i = dp[i - 1][j - volume_[i]] + value_[i] if j >= volume_[i] else 0
        dp[i][j] = max(no_i, add_i)
print(f"last is : {dp[thing_num - 1][all_capa]}")
