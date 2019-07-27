r1,r2=input().split()
r3=abs(len(r2)-len(r1))
for g in range(len(r1)):
    if(len(r2)==1 and r2[g] in r1):
        break
    if (r1[g]!=r2[g]):
        r3=r3+1
print(r3)
