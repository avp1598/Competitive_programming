import math
def simple_sieve(n):
    primes=[]
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
         
        if (prime[p] == True):
             
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            primes.append(p)
            
    return primes
    
def segmented_sieve(mi,ma):
    primes= simple_sieve(int(math.sqrt(ma))+1)
    is_prime = [True for i in range(mi,ma+1)]
    for p in primes:
        i=int(math.ceil(float(mi)/p))
        while i <= math.ceil(ma/p):
            is_prime[i*p-mi] = False
            #print "p=",p,"i=",i,is_prime[213]
            i+=1
    j=1
    
    for i in primes:
        if i >= mi:
            print i
            
    for i in range(ma-mi+1):
        if is_prime[i]:
            if i+mi!=1:
                print i+mi
            j+=1
            
     


t=input()
arr = []
for i in range(t):
    arr.append(raw_input())


for i in range(t):
      mi,ma=arr[i].split()
      segmented_sieve(int(mi),int(ma))
      
      print "\n"
    
