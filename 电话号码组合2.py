from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.s = ""
        self.letterMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.res
        self.backtracking(digits, 0)

    def backtracking(self, digits, index):
        if index == len(digits):
            self.res.append(self.s)
            return
        digit = int(digits[index])
        letter = self.letterMap[digit]
        for i in range(len(letter)):
            self.s += letter[i]
            self.backtracking(digits, index + 1)
            self.s = self.s[:-1]


s = Solution()
print(s.letterCombinations("23"))
print(s.res)
