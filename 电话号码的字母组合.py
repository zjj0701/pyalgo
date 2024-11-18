from typing import List

letterMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
result = []
s = ""


def backtracking(digits, index, s):
    if index == len(digits):
        result.append(s)
        return
    digit = int(digits[index])
    letters = letterMap[digit]
    for i in range(len(letters)):
        s += letters[i]
        backtracking(digits, index + 1, s)
        s = s[:-1]


def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0:
        return result
    backtracking(digits, 0, s)


print(letterCombinations(digits="23"))
print(result)
