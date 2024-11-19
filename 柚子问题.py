import sys
from typing import List


def backtrace(i: int, r: int):
    global maxR
    for j in range(x[i * 2] * (m - 1) + 1):
        if y[j] < m:
            for k in range(1, m - y[j] + 1):
                if y[i] + k < y[j + x[i - 1] * k]:
                    y[j + x[i - 1] * k] = y[j] + k

    while y[r] < maxint:
        r += 1
    if i > n:
        if r - 1 > maxR:
            maxR = r - 1
            for j in range(1, n + 1):
                bestx[j] = x[j]
        return
    z: List[int] = [] * (maxl + 1)
    for k in range(1, maxl + 1):
        z[k] = y[k]
    for j in range(x[i - 1] + 1, r + 1):
        if y[r - j] < m:
            x[i] = j
            backtrace(i + 1, r + 1)
            for k in range(1, maxl + 1):
                y[k] = z[k]

maxR: int = 0  # 当前最优值
if __name__ == '__main__':
    n: int = 5
    m: int = 4
    maxint = sys.maxsize
    maxl: int = 0  # 邮资上界
    x: List[int] = [0] * n  # 当前解
    y: List[int] = [maxint] * (n + 1)  # 最少邮票数
    x[1] = 1
    y[0] = 0
    bestx: List[int] = []  # 最优解
    backtrace(2, 1)
    print(maxR)
