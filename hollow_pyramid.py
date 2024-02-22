n=int(input())
rows=2*n-1
sp=n-1
spk=1
num=1
for i in range(rows):
    if i==0 or i==rows-1:
        st=1
    else:
        st=2
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
    print()
    if i<n//2:
        sp-=1
        num+=1
    else:
        sp+=1
        num-=1
