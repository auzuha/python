l = []
def minus(s,c):
    a = '';co=0;
    for i in s:
        if i == c and co == 0:
            pass
            co += 1
        else:
            a += i
    return a
            
count = 0
def f(s,upto):    
    global l
    global count
    count += 1
    if s == '':
        if upto not in l:
            l.append(upto)
            
            
        return
        #print(upto)
    for i in s:
        #f(s.replace(i,''),upto+i)
        f(minus(s,i),upto+i)
s = 'aaacc'.lower()
upto = ''
f(s,upto)
print(len(l))
#print(l)
print(count)
for i in l:
    print(i)