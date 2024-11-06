g = [10,9,8,7]  # 胃口
s = [5,6,7,8]  # 饼干
g.sort()
s.sort()
print(g)
print(s)
res = 0
index = 0
for i in range(len(s)):
    if index<len(g) and s[i]>=g[index]:
        res+=1
        index+=1
print(res)