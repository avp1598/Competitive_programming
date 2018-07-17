import math
from sys import stdin, stdout

def F(x,c,pos):
    last_pos=0
    c-=1
    for i in xrange(1,len(pos)):
        if pos[i]-pos[last_pos]>=x:
            c-=1
            last_pos=i
        if c==0:
            return True

    return False

def min_dist(pos,c):
    #print F(2,c)
    low=0
    high=pos[-1]-pos[0]+1
    #print "high=",high
    ans=1
    while high-low>0:
        mid=(high+low)/2
        #print "mid=",mid
        if F(mid,c,pos):
            if mid>ans:
                ans=mid
            low=mid+1
        else:
            high=mid-1
            
    if F(low,c,pos):
       print low
       return

    print ans

#t=input()
t=int(stdin.readline())

pos = []
c=[]
app1=c.append
app2=pos.append
for i in xrange(t):
    #p,temp=raw_input().split()
    p,temp=stdin.readline().split()
    p=int(p)
    temp=int(temp)
    app1(temp)
    lt=[]
    app3=lt.append
    for i in xrange(p):
        #app3(int(raw_input()))
        app3(int(stdin.readline()))
    app2(lt)



for i in xrange(t):
    pos[i].sort()
    min_dist(pos[i],c[i])
    #F(500000,c[i],pos[i])




        
    
