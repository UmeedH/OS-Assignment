arr = []
bt=[]
wt=[]
wtotal=0
n = int(raw_input('Enter the total no of processes: '))
atime=(int(raw_input('Enter parrival time: ')))
for i in xrange(n):
    arr.append([])
    arr[i].append(int(raw_input('Enter pnumber: ')))
    #pbust = 
    bt.append(int(raw_input('Enter pbust time: ')))
j=1
for i in xrange(n):
    post=i
    for j in xrange(n):
        if bt[j]<bt[post]:
            post=j
        temp=bt[i]
        bt[i]=bt[post]
        bt[post]=temp
        temp=arr[i]
        arr[i]=arr[post]
        arr[post]=temp
wt.append(0)
j=0
for i in xrange(n):
    wt.append(0)
    for j in xrange(i):
        wt[i]+=bt[i]
    wtotal+=wt[i]
print 'ProcessNumber\tArrivalTime\tBurstTime\tWaiting Time'
for i in xrange(n):
    print arr[i],'\t\t',atime,'\t\t',bt[i], '\t\t',wt[i]
    
print 'Total waiting time: ',wtotal
print 'Average waiting time: ',(wtotal/n)
