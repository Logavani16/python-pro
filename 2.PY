from itertools import combinations
numb ,r1 = input().split()
r1 = int(r1)
r2 = []
hj = combinations(numb,len(numb)-r1)
for d in hj:
    r2.append("".join(d))
print(min(r2))
