def ysfh(N,K,M):
    lst =[i for i in range(1,N+1)]
    count=N
    num=K
    while True:
        if len(lst)==2:
            return
        num=(num+M)%count
        count-=1
        print(lst[num],end='->')
        del lst[num]


N=int(input('一共有多少个人：'))
K=int(input('从什么编号开始报数：'))
M=int(input('数到M，此人出列：'))
ysfh(N,K,M)
