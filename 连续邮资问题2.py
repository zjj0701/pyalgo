maxl = 1000  # 最大的连续值
maxint = 32767
n = 5  # 邮票数
m = 4  # 最大张数
maxvalue = 0  # 最大的连续值
bestx = [0] * 1000  # 最优解
y_maxl = [maxint] * maxl  # y[k]，存储表示到k值，所使用的最少的邮票数
x = [0] * 100
x[1] = 1
y_maxl[0] = 0


def backtrace(i, r):
    global maxvalue
    # 对上一层邮资数组更新，上限时x[i-1]*m
    for j in range(x[i - 1] * m + 1):
        if y_maxl[j] < m:
            # 从只是用一个x[i]到使用m-y[i]个，即使用最多的最大值，降低邮票数
            # k是对表示j剩余的票数进行检查
            for k in range(1, m - y_maxl[j] + 1):
                if y_maxl[j] + k < y_maxl[j + x[i] * k]:
                    # 如果前面的某一个情况加上k个x[i],所达到邮资值的使用邮票数少于原来邮票数则更新
                    y_maxl[j + x[i] * k] = y_maxl[j] + k
    # 向后寻找最大的邮资值，查看邮资范围扩大多少，查询y数组找到r
    while y_maxl[r] < maxint:
        # 计算X[1:i]的最大连续邮资区间
        r += 1
    if i == n:  # i==n 表示到达了叶子节点
        if r - 1 > maxvalue:  # 如果大于最大值，更新最优值与最优解
            for l in range(1, n + 1):
                bestx[l] = x[l]
            maxvalue = r - 1
        return
    # 每一层要对多种情况进行运算，将上一层的邮资数组保存
    z = [0] * maxl
    for k in range(maxl):
        z[k] = y[k]
    # 对下一层进行运算
    for j in range(x[i] + 1, r + 1):
        x[i + 1] = j
        backtrace(i + 1, r - 1)
        for k in range(maxl):
            y[k] = z[k]

if __name__ == '__main__':
    backtrace(1, 0)
    print(f"当前最优解")
    # for i in range(1, maxl + 1):
    #     print(f"best is:{bestx[i]}")
    print(f"最大连续的邮资时：{maxvalue}")


