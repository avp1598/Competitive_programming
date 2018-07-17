from sys import stdin, stdout

n,h=stdin.readline().split()
st=stdin.readline().split()
st= map(int, st)
cmd=stdin.readline().split()
pos=[1,0]

for i in cmd:
    if i=='1':
        if pos[0]>1:
            pos[0]-=1
    elif i=='2':
        if pos[0]<int(n):
            pos[0]+=1
    elif i=='3':
        if st[pos[0]-1]>0 and pos[1]!=1:
            st[pos[0]-1]-=1
            pos[1]=1
    elif i=='4':
        if st[pos[0]-1]<int(h) and pos[1]!=0:
            st[pos[0]-1]+=1
            pos[1]=0
    '''
    print "cmd=",i
    print "pos= ",pos
    print "stk= ",st
    print ""
    '''
for p in st: print p,
            
        
    
        
    
