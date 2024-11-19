Max = 4
Prices = [0, 1, 3, 11, 15, 32]

def TraceBack(count, tmp):
    global result
    # 如果选择的数量已经达到 Max，检查当前总和是否大于 result
    if count == Max:
        result = max(result, tmp)
        return
    for i in range(len(Prices)):
        if tmp + Prices[i] <= result:  # 如果当前总和不超过 result
            TraceBack(count + 1, tmp + Prices[i])  # 递归，选择该价格
        # 这里不需要撤销 tmp，因为传递的是新的 tmp

result = 0
# 递归开始，模拟选择最多 Max 个价格的所有组合
while True:
    tmp = 0
    TraceBack(0, tmp)  # 从0开始
    if result:  # 如果 result 非零，表示找到了有效的组合
        result += 1
    else:
        break

print(result)
