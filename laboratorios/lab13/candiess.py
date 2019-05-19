def candy(N,r):
    H=[0]*N
    R=r
    cur_can=1
    cand=[0]*N
    cand[0]=1
    #print R#,'\n',cand
    for i in range(0,N):
        if i!=0:
            #print R[i],'  ',R[i-1]
            if R[i]>R[i-1]:
                cand[i]=cand[i-1]+1
            else:
                cand[i]=1
##            print R[i],i
    sum=0
##    print i
    print (cand)
    for j in range(0,N):
        sum+=cand[j]
    return sum
r=[int(x)for x in stdin.readline().strip().split()]
N=len(r)
print (candy(N,r))
