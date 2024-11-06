g = [1,2,3]  # 胃口
s = [3]  # 饼干
g.sort()
s.sort()
print(g)
print(s)
res = 0
index = len(s)-1
for i in range(len(g)-1,-1,-1):
    if index >0 and  s[index]>=g[i]:
        res+=1
        index-=1
print(res)