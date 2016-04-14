arr = []
twait = 0
n = int(raw_input('Enter the total no of processes: '))
for i in xrange(n):
    arr.append([])
    arr[i].append(raw_input('Enter pname: '))
    arr[i].append(int(raw_input('Enter parrival time: ')))
    twait += arr[i][1]
    arr[i].append(int(raw_input('Enter pbust time: ')))

arr.sort(key = lambda arr:arr[1])

print 'ProcessName\tArrivalTime\tBurstTime'
for i in xrange(n):
    print arr[i][0],'\t\t',arr[i][1],'\t\t',arr[i][2]
    
print 'Total waiting time: ',twait
print 'Average waiting time: ',(twait/n)
