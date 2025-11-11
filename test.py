arr = [10, 5, 10]
arr.sort()
n = len(arr)
max_num = arr[n-1]
for i in range(0,n-1,-1):
    print(arr[i])
    #if max_num != arr[i]:
        #print( arr[i])
#print(-1)