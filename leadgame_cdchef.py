from sys import stdin, stdout

r=int(stdin.readline())
max_lead=0
max_player=1
sum1=0
sum2=0

for i in xrange(r):
    s1,s2=stdin.readline().split()
    sum1+=int(s1)
    sum2+=int(s2)
    lead=abs(sum2-sum1)
    if lead>max_lead:
        max_lead=lead
        if sum2>sum1:
            #print "s2=",s2
            #print "s1=",s1
            max_player=2
        else:
            max_player=1

print max_player,max_lead

    


    
