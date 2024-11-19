maxl = 1000  # 最大邮资范围
maxint = 32767  # 一个较大的值，表示不可达的情况
n = 5  # 邮票种类数
m = 4  # 每种邮票的最大使用张数
maxvalue = 0  # 最大连续邮资值
bestx = [0] * 100  # 最优解，记录最优邮票组合
y_maxl = [maxint] * maxl  # y[k] 表示到 k 值的最小邮票数
x = [0] * 100  # 存储当前邮票组合
x[1] = 1  # 第一种邮票固定为 1
y_maxl[0] = 0  # 邮资为 0 时不需要邮票


def backtrace(i, r):
    global maxvalue
    # 更新邮资数组
    for j in range(x[i - 1] * m + 1):  # 遍历上一层的邮资范围
        if y_maxl[j] < m:  # 如果当前邮资值可达且使用票数小于最大张数
            for k in range(1, m - y_maxl[j] + 1):  # 尝试使用 k 张当前邮票
                new_postage = j + x[i] * k
                if new_postage < maxl and y_maxl[j] + k < y_maxl[new_postage]:
                    y_maxl[new_postage] = y_maxl[j] + k

    # 寻找当前最大连续邮资值
    while r < maxl and y_maxl[r] < maxint:
        r += 1

    if i == n:  # 叶子节点：如果当前邮票组合完成
        if r - 1 > maxvalue:  # 如果找到更大的连续邮资区间
            for l in range(1, n + 1):
                bestx[l] = x[l]  # 保存当前最优邮票组合
            maxvalue = r - 1  # 更新最大连续邮资值
        return

    # 保存当前邮资数组状态（回溯）
    z = y_maxl[:]

    # 遍历下一层邮票值，注意邮票值需比上一层邮票大
    for j in range(x[i] + 1, r):  # 限制为大于当前邮票值的范围
        x[i + 1] = j
        backtrace(i + 1, r - 1)  # 递归进入下一层
        y_maxl[:] = z  # 恢复邮资数组状态


if __name__ == '__main__':
    backtrace(1, 1)
    print("当前最优解:")
    print(f"邮票种类: {bestx[1:n + 1]}")
    print(f"最大连续邮资值: {maxvalue}")
