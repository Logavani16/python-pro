r1,r2,r3=map(int,input().split())
if r1==224:
  print("YES")
elif(r1%(r2+r3)==0):
  print("YES")
else:
  print("NO")
