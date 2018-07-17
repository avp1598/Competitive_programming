from sys import stdin, stdout
l1,l2,l3=stdin.readline().split()
a=set()
b=set()
c=set()

for i in xrange(int(l1)): a.add(stdin.readline().strip())
for i in xrange(int(l2)): b.add(stdin.readline().strip())
for i in xrange(int(l3)): c.add(stdin.readline().strip())

#print a,b,c
#print a&b
#print b&c
#print c&a

ans=(a&b)|(b&c)|(c&a)
print 
print len(ans)
for i in sorted(ans): print i
