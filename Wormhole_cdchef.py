from sys import stdin, stdout

def binary_search1(arr, val):
    #print val
    high=len(arr)-1
    low=0
    ans=0
    while high-low>=0:
        mid=(high+low)/2
        if val==arr[mid]:
            return arr[mid]
        elif val>arr[mid]:
            low=mid+1
            if arr[mid]>ans:
                ans=arr[mid]
        else:
            high=mid-1

    return ans

def binary_search2(arr, val):
    #print val
    high=len(arr)-1
    low=0
    ans=1000000
    while high-low>=0:
        mid=(high+low)/2
        #print high,low,mid
        if val==arr[mid]:
            return arr[mid]
        elif val<arr[mid]:
            low=mid+1
            if arr[mid]<ans:
                ans=arr[mid]
        else:
            high=mid-1

    return ans

n,xl,yl=map(int,stdin.readline().split())
cs=[]
for i in xrange(n):
    cs.append(map(int,stdin.readline().split()))

x=map(int,stdin.readline().split())
y=map(int,stdin.readline().split())
x.sort()
y.sort(reverse=True)
ma=100000


for test in cs:
   st=binary_search1(x,test[0])
   et=binary_search2(y,test[1])
   if et-st+1<ma:
        ma=et-st+1
        ans=[]
        ans.append(st)
        ans.append(et)

print ans[1]-ans[0]+1

            
   
