class Stamp:
    def __init__(self, n, m):
        self.n = n  # 邮票种类数
        self.m = m  # 每张信封最多允许贴的邮票数
        self.maxvalue = n  # 当前已找到的最大连续邮资区间
        self.bestx = []  # 当前最优解，即邮票面值组合
        self.y = [float('inf')] * (n * m + 1)  # y[k]表示贴出邮资k所需的最少邮票数
        self.x = []  # 当前邮票面值组合

    def backtrack(self, i, r):
        if i > self.n:
            # 到达叶子节点，检查是否找到更好的解
            if r - 1 > self.maxvalue:
                self.maxvalue = r - 1
                self.bestx = self.x[:]
            return

        # 当前节点是内部节点，扩展子节点
        for val in range(self.x[i - 1] + 1 if i > 1 else 2, r + 1):
            if self.y[val - 1] <= self.m:  # 确保能用前面的邮票组合支付当前邮资
                self.x.append(val)
                prev_y = self.y[:]
                # 更新y数组
                for j in range(val, self.y[-1]):
                    if self.y[j - val] < self.m:
                        self.y[j] = min(self.y[j], self.y[j - val] + 1)

                # 继续搜索
                self.backtrack(i + 1, r)

                # 回溯
                self.y = prev_y
                self.x.pop()

    def solve(self):
        self.x = [1]  # 第一张邮票面值必须为1
        self.y[0] = 0  # 邮资0需要0张邮票
        self.y[1] = 1  # 邮资1需要1张邮票
        for i in range(2, self.m + 1):
            self.y[i] = 1  # 用1面值的邮票支付1到m的邮资
        self.backtrack(2, self.m)  # 从第二张邮票开始
        return self.maxvalue, self.bestx


# 使用示例
n = 5  # 邮票种类数
m = 4  # 每张信封最多允许贴的邮票数
problem = Stamp(n, m)
max_value, best_solution = problem.solve()
print("最大连续邮资区间:", max_value)
print("最佳邮票面值设计:", best_solution)

