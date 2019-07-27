r1,r2=map(str,input().split())
r3=0
if len(r1)>len(r2):
  r1,r2=r2,r1
r=0
while r<len(r1):
  r3+=(ord(r2[r])-ord(r1[r]))
  r+=1
for r in range(r,len(r2)):
  r3+=ord(r2[r])-ord('a')+1
print(r3)
