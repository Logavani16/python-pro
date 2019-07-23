r1=int(input())
r2=[]
for h in range(0,r1):
 pan=input()
 r2.append(pan)
r3=[]
for h in zip(*r2):
 if(h.count(h[0])==len(h)):
  r3.append(h[0])
 else:
  break
print(''.join(r3))
