from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.sum_ = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return self.res
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.res

    # candidates = [2,3,6,7], target = 7
    def backtracking(self, candidates, target, index, sum_):
        if target == sum_:
            self.res.append(self.path[:])
            return
        if target < sum_:
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if sum_ + candidates[i] > target:
                break
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, i + 1, sum_)
            sum_ -= candidates[i]
            self.path.pop()


s = Solution()
s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
print(s.res)
