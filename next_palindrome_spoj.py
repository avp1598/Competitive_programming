def is_pal(num):
    if num[::-1]==num:
        return True
    else:
        return False

def if_pal(num):
    l=len(num)
    if l%2==1:
        if num[l/2]!='9':
            new=num[:l/2]+str(int(num[l/2])+1)+num[l/2+1:]
        else:
            new=str(int(num[:l/2])+1)+'0'+str(int(num[l/2+1:][::-1])+1)[::-1]
            if len(new)>l+1:
                new=new[:l/2]+new[l/2+1:]
    else:
        if num[l/2]!='9':
            new=num[:l/2-1]+str(int(num[l/2-1])+1)+str(int(num[l/2])+1)+num[l/2+1:]
        else:
            new=str(int(num[:l/2])+1)+str(int(num[l/2:][::-1])+1)[::-1]
            if len(new)>l+1:
                new=new[:l/2]+new[l/2+1:]
            
    print new

def next_pal(num):
    #case 1
    if num=="9":
        print "11"
        return
    #case 2
    if is_pal(num):
        if_pal(num)
        
    #case 3
    else:
        l=len(num)
        if l%2==1:
            new=num[:l/2]+num[l/2]+num[:l/2][::-1]
            if num[:l/2][::-1] < num[l/2+1:]:
                if_pal(new)
            else:
                print new
        else:
            new=num[:l/2]+num[:l/2][::-1]
            if num[:l/2][::-1] < num[l/2:]:
                if_pal(new)
            else:
                print new
        
            


        
t=input()              
arr = []
for i in range(t):
    arr.append(raw_input())

for i in range(t):
      next_pal(arr[i])
