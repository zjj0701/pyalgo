k = 9  # 个数
n = 45  # 总和

res = []
tmp = []
all = 0


def backtracking(n, k, all, index):
    global tmp
    global res
    if len(tmp) == k:
        if all == n:
            res.append(tmp[:])
        return

    for i in range(index, 10):
        tmp.append(i)
        all += i
        if all > n:
            all -= i
            tmp.pop()
            return
        backtracking(n, k, all, i + 1)
        all -= i
        tmp.pop()


backtracking(n, k, all, 1)
print(res)
