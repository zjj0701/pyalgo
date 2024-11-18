from typing import List

'''
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
'''


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.sum = 0

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return self.res
        self.backtracking(s, 0)
        return self.res

    def backtracking(self, s, index):
        if index >= len(s):
            self.res.append(self.path[:])
            return
        for i in range(index, len(s)):
            print(f"当前index是{index},当前i是{i},当前切片{s[index: i + 1]},当前sum{sum}")
            if self.is_hw(s, index, i):
                self.path.append(s[index: i + 1])
                self.backtracking(s, i + 1)
                self.path.pop()
            else:
                continue

    def is_hw(self, s, start, end):
        i = start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


s = Solution()
s.partition("aab")
print(s.res)
