import copy
from typing import List

n = 4
k = 2

res = []
tmp = []


def backtracking(n, k, startIndex):
    if len(tmp) == k:
        # ll = copy.deepcopy(tmp) 测试中发现时间消耗巨大
        res.append(tmp[:])  # 切片复制
        return
    for i in range(startIndex, n):
        tmp.append(i)
        backtracking(n, k, i + 1)
        tmp.pop()


def combine(n: int, k: int) -> List[List[int]]:
    startIndex = 1
    backtracking(n + 1, k, startIndex)


combine(n, k)
print(res)
